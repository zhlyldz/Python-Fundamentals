from pprint import pprint
from requests import get

response=get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bb41a28377ac414bb0700f30b60edbb6")

business_headlines = response.json()

pprint(business_headlines)

author = business_headlines.get("articles")[1].get("author")
title =business_headlines.get('articles')[1].get('title')
published_at =business_headlines.get('articles')[1].get('publishedAt')

print(f'Author: {author}')
print(f'Title: {title}')
print(f'Published Date: {published_at}')

Kullanıcıdan author name bilgilerine göre ilgili makale yazdırılsın
author_name=input("author_name: ")

for article in business_headlines.get("articles"):
    if article.get("author")==author_name:
        pprint(article)

