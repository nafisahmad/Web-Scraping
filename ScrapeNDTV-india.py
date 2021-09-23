# import
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.ndtv.com/india/page-1')
# print(res)

soup = BeautifulSoup(res.text, 'html.parser')   
# print(soup)
# print(soup.body.contents)
# print(soup.title)

# print(soup.find(class_='newsCont'))
# print(soup.select('.newsCont'))

# print(soup.select('.news_Itm')[0])
# print(soup.select('#text'))

links = soup.select('.news_Itm')
date = soup.select('.postedby')
# print(links[1].get('.newsCont'))

def create_custom(links, date):
    hn=[]
    for idx,item in enumerate(links):
        title = links[idx].getText()
        span = links[idx].get('span', None)



        hn.append({'News': title, 'dated': span})
    return hn

pprint.pprint(create_custom(links, date))




