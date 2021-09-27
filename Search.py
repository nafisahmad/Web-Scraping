# import
import requests
from bs4 import BeautifulSoup
import pprint
import re

res = requests.get('https://inshorts.com/en/read/national')
# print(res)

soup = BeautifulSoup(res.text, 'html.parser')   
# print(soup)
# print(soup.body.contents)
# print(soup.title)

# print(soup.find(class_='newsCont'))
# print(soup.select('.newsCont'))

# print(soup.select('.news_Itm')[0])
# print(soup.select('#text'))

# print(soup.find_all(string=re.compile("health")))

links = soup.select('.news-card')
links = soup.find_all(string=re.compile("health"))
print(soup.find_all(string=re.compile("health")))
# date = soup.select('.date')
# # print(links[1].get('.news-card-content'))

# def create_custom(links, date):
#     hn=[]
#     for idx,item in enumerate(links):
#         title = links[idx].getText()
#         span = links[idx].get('date', None)

#         hn.append({'News': title, 'dated': span})
#     return hn

# pprint.pprint(create_custom(links, date))
