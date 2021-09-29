import re
import requests
from bs4 import BeautifulSoup


url = "https://inshorts.com/en/read/national"
api_url = "https://inshorts.com/en/ajax/more_news"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
}

# load first page:
html_doc = requests.get(url, headers=headers).text
min_news_id = re.search(r'min_news_id = "([^"]+)"', html_doc).group(1)

pages = 10  # <-- here I limit number of pages to 10
while pages:
    soup = BeautifulSoup(html_doc, "html.parser")

    # search the soup for your articles here
    # ...

    # here I just print the headlines:
    for headline in soup.select('[itemprop="headline"]'):
        # print(headline.text)
        print(len(headline))

    # load next batch of articles:
    data = requests.post(api_url, data={"news_offset": min_news_id}).json()
    html_doc = data["html"]
    min_news_id = data["min_news_id"]

    pages -= 1