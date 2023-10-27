
# Dictionary (Sözlük)
# Sözlük objesi, list, tuple gibi geçici olarak verileri depolayabildiğimiz başka bir yapıdır.
# Sözlükler 'key' & 'value' mantığında çalışırlar.
# Anahtarlar herhangi bir değere erişmek için kullanılırlar.

my_dict = {
	'Full Name': 'Burak Yılmaz',
	'Age': 34,
	'Sports': ['Boxing', 'UFC', 'Wrestling', 'NBA', 'NFL'],
	'User Names': ('beast', 'savage', 'crayz bear'),
	'Books': {
		'War History': 'Cambridge War History',
		'Scientfic': {
			'Karl Poper': 'The Logic of Scientfic Discovery'
		}
	}
}

release_year_movies = {
	'Fight Club': 1999,
	'Matrix': 1999,
	'Interstaller': 2014,
	'Inception': 2010,
	'Dune': 2021
}

# Herhangi bir filmin anahtarın çağarak değerini ekrana yazın
# Yol I
print(f'Interstaller Release Year: {release_year_movies.get("Interstaller")}')
# Yol II
print(f'Interstaller Release Year: {release_year_movies["Interstaller"]}')


# Sözlüğün bütün anahtarlarını dökün
for i in release_year_movies.keys():
	print(i)

# Sözlüğün tüm değerlerini dökün
print([i for i in release_year_movies.values()])


from pprint import pprint
pprint({name: year for name, year in release_year_movies.items()})


products = [
	{
		'name': 'Everlast Pro Boxing Gloves',
		'price': 245
	},
	{'name': 'Everlast Training Gloves', 'price': 200},
	{'name': 'Everlast Havy Bag', 'price': 345},
	{'name': 'Everlast Hand-Wrap', 'price': 56},
	{'name': 'Iphone 14 Pro Max', 'price': 48000},
	{'name': 'Samsung G20', 'price': 40000},
	{'name': 'Lenovo x1 Carbon', 'price': 49000},
]

# products listesinde ki bütün fiyatları toplayarak ekrana basın
total_price = 0
for product in products:
	total_price += product.get('price')
	
print(f'Total: {total_price}')


# products listesinde ki ürün fiyatı 30000'den büyük olan ürünlerin isimlerini listeleyiniz
for product in products:
	if product['price'] >= 30000:
		print(product['name'])

# Ürün adı içerisinde Everlast geçen ve fiyat aralığı 150 ile 300 arasında olan ürünleri listeleyiniz
for product in products:
	if 'Everlast' in product['name'] and 150 <= product['price'] <= 300:
		print(product['name'])

# boş bir student sözlüğü oluşturalım.
# Kullanıcı exit diyene kadar istediği kadar işlem yapabilsin.
# Kullanıcıdan yapmak istediği işlemi isteyelim. işlemler => exit, create, read, update, delete
# Not: YUkarıda ki işlemlere kısaca CRUD denir.
# Kullanıcının yapacağı işlemlere göre inputlar alarak işlemleri gerçekleştirelim.
# CRUD operasyonlarında 'student_id' anahtarından ilerlerin.
# students = {
# 	'student_id': {
# 		'first_name': 'fsdfds',
# 		'last_name': 'fdsfs',
# 		'phone': 'fdsfd'
# 	}
# }

students = {}

while True:
	process = input('Choose your process: ').lower()
	if process == 'exit':
		break
	elif process == 'create':
		# şimdi kullanıcıdna input alınıyor: id, first name, last name, phone
		student_id = input('Id: ')
		first_name = input('First Name: ')
		last_name = input('Last Name: ')
		phone = input('Phone: ')
		# students sözlüğüne ekle
		# bir sözlüğe bir item eklemek için eklenecek item dictionary tipinde olmasını istediğimiz için inputlardan bir sözlük oluşturuyoruz.
		students[student_id] = {
			'first_name': first_name,
			'last_name': last_name,
			'phone': phone
		}
	elif process == 'list':
		pprint(students)
	elif process == 'update':
		student_id = input('Id: ')  # Update edilecek öğrencinin id'sini kullanıcıdan alıyoruz.
		first_name = input('First Name: ')
		last_name = input('Last Name: ')
		phone = input('Phone: ')
		
		students.update({
			student_id: {
				'first_name': first_name,
				'last_name': last_name,
				'phone': phone
			}
		})
	elif process == 'delete':
		student_id = input('Id: ')
		del students[student_id]
		
















