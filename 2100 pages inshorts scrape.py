import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm  import tqdm
# code for scraping the first page
d={'headlines':[],'news':[]}
r = requests.get("https://inshorts.com/en/read")
soup = BeautifulSoup(r.content, 'html.parser')
min_news_id = soup.findAll("script",{"type":"text/javascript"})[2].text
min_news_id = min_news_id[25:35]
soup=soup.findAll("div",{"class":"news-card z-depth-1"})
for data in soup:
    d['headlines'].append(data.find(itemprop="headline").getText())
    d['news'].append(data.find(itemprop="articleBody").getText())
# code for scraping more pages
for i in tqdm(range(2100)):
# It uses JavaScript to load more data from
# https://inshorts.com/en/ajax/more_news using POST requests
# with parameter 'news_offset' which informs server what page
# it has to send to client.
# we can make POST requests with this parameter to get new
# data in JSON format
    try:
        params = {'news_offset': min_news_id}
        req = requests.post("https://inshorts.com/en/ajax/more_news",data=params)
#In JSON you have HTML in json_data['html'] and
#json_data['min_news_id'] for next page

        json_data = req.json()
        min_news_id = json_data['min_news_id']
        soup = BeautifulSoup(json_data['html'], 'html.parser')
        soup=soup.findAll("div",{"class":"news-card z-depth-1"})
        for data in soup:
            d['headlines'].append(data.find(itemprop="headline").getText())
            d['news'].append(data.find(itemprop="articleBody").getText())
    except:
        pass
# storing the data into .csv file
df = pd.DataFrame(d)
df.to_csv("inshorts_news.csv", index=False)