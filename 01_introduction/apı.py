

# API'lerden hızlıca veri talebinde bulunmak için python içerisinde bulunan 'request' modülünden faydalanacağız. Bugün kullanacağımı API (Application Programming Interface) free'dir. Yani API'ler ücretli olarak veri temin etmektedir.
# API'leri günlük hayatımızda yoğun olarak kullanmaktayız. web sitelerinde hava durumu genellikle OpenWeatherAPI gelen veri ile oluşturulur. Facebook, Google apileri kullanılarak 3rd uygulamalar geliştirebiliyoruz. Gene apileri kullanarak basit oyunlar tasarlayabiliriz.
# Günümüzde çok popüler olan ChatGPT'de bir apidir. Sizlerden gelen talebi backend iletir.
# Bu çalışmada free NewsAPI'den Tesla ile alakalı makaleleri çekeceğiz. BU işlem için 'https://newsapi.org/' sitesine login olup bir api key aldık. Bu 'key' bize veri çekme olanağı verecektir.

from pprint import pprint
# request modülü python core dosyaları arasında bulunmamaktadır. Bu yüzden bu modülü yüklememiz gerekmektedir.
# bunun için 'terminal' ekranına gelere 'pip install requests' diyebilir yada ilgili modülü yüklediğimiz satıra gelip yüklem işlemini GUI üzerinden yerine getirebiliriz.
# python'da harici bir modül ile ilgili bilgi almak istersek bakacağımız site ise 'https://pypi.org/'
from requests import get

# requests modülünü kullanarak ilgili api'ye talep (request) atacağız. bu talep sonucunda bize bir cevap (response) döner.
response = get("https://newsapi.org/v2/everything?q=tesla&from=2023-04-20&sortBy=publishedAt&apiKey=ca18aebd834a4afbb53385bb02b899bd")

# Günümüzde internetin çalışma mantığı çok basittir. Kullanıcılar, bir web sitesine talepte (request) ve web siteside bir cevap (response) döner. Bu mantığa HTTP Protokolü denir. Bu protokolün mantığına göre yukarıda api'ye http request attık.

tesla_data = response.json()
# Json (Javascript Object Notation), değişik platformlarda koşan yani çalışan uygulamaların kendi aralarında veri transferi yaparken kullandıkları bir notasyondur.

pprint(tesla_data)

author = tesla_data.get('articles')[1].get('author')
title = tesla_data.get('articles')[1].get('title')
published_at = tesla_data.get('articles')[1].get('publishedAt')

print(f'Author: {author}')
print(f'TiTle: {title}')
print(f'Published Date: {published_at}')


# Kullnıcıdan yazar ismi alınacak, alınan bu yazar ismine göre ham data search edilecek
# İlgili yazarın makalesi ekrana basılacak
author_name = input('Author name: ')
for article in tesla_data.get('articles'):
	if article.get('author') == author_name:
		pprint(article)