# Python'da bir obje yaratmak için "class" kullanıyoruz.
# bu sınıflar içerisinde yaratacağımız objenin özelliklerini değişken tanımlar gibi içerisinde tanımlıyoruz.
# sınıfları (class) gerçek dünyada ki prototiplere benzetebiliriz.
class Vehicle:
	door_numbers = 4
	brand = ''
	model = ''
	engine_size = ''
	torque = ''


vehicle_1 = Vehicle()  # burada sınıfımızdan örneklem (instance) çıkardık. instance aldığımızda ilgili sınıfın özelliklerine sahip bir obje yaratmış oluruz.
print(type(vehicle_1))
vehicle_1.torque = 1.2
vehicle_1.brand = 'Dodge'
vehicle_1.model = 'TRX1500'
vehicle_1.engine_size = 5.4
# vehicle_1.door_numbers özelliğine değer atamadık çünkü default değerini kullanıyoruz.
print(f"""
Brand: {vehicle_1.brand}
Model: {vehicle_1.model}
Engine Size: {vehicle_1.engine_size}
Torque: {vehicle_1.torque}
Door Numbers: {vehicle_1.door_numbers}
""")


# Bir sınıftan örneklem (instance) aldığımızda sınıf_adı() kullanıyoruz. Yani instance aldığımızda aslında sınıfın init() fonksiyonunu tetikliyoruz. init() fonksiyonu otomatik olarak knedisi tetiklenir. Bir sınıfı başlatamaya (initialize) yarar. Yani sınıfı kullanıma hazırlar. Bir diğer yeteneği ise sınıf ayağı kalkarken dışarıdan gelen değerleri sınıfın özelliklerine atar. Böylelikle sınıftna insatance alınırken obje belirli özelliklerle yaratılmış olur.
class Boxer:
	# class attribute
	takma_ad = ''
	
	def __init__(self, age, first_name, last_name, record):
		# init içerisinde tanımladığımız özelliklere object attribute diyebilir miyiz?
		self.yas = age
		self.adi = first_name
		self.soyadi = last_name
		self.record = record
		self.ko = ''


mike_tyson = Boxer(34, 'Burak', 'Yılmaz', 3)
print(f"""
Adı: {mike_tyson.adi}
Soyadi: {mike_tyson.soyadi}
K.O: {mike_tyson.ko}
""")


# Circle isminde bir sınıf yaratalım
# pi adında bir class attribute yaratalım
# r adında bir object attribute yaratalım
# alan ve çevre hesaplama yetenekleri fonksiyonları ekleyelim
# class Circle:
# 	pi = 3.14
#
# 	def __init__(self, radius):
# 		self.r = radius
#
# 	def calculate_area(self):
# 		return self.pi * self.r ** 2
#
# 	def calculate_perimeter(self):
# 		return 2 * self.pi * self.r
#
#
# r = float(input('Radius: '))
# c1 = Circle(r)
# print(c1.calculate_area())
# print(c1.calculate_perimeter())


# Teacher adında bir sınıf oluşturalım
# first_name, last_name object attribute olsun
# kullanıcı değer girmezse exception yemeyelim
# sınıf içeirisnde öğrentmenin bilgilerini ekrana basan bir foksiyon yazın
# class Teacher:
# 	def __init__(self, first_name='', last_name=''):
# 		self.full_name = first_name + ' ' + last_name
#
# 	def show_info(self):
# 		print(f'Full Name: {self.full_name}')
#
#
# t1 = Teacher(
# 	input('Please type first name:'),
# 	input('Please type last name: ')
# )
# t1.show_info()


# Departmant adında bir sınıf oluşturalım
# departmant_name ve employee_count => class attribute
# name, age => object attribute
# show_info()
# show_employee_count()
# her bir çalışlan yaratıldığında person_count otomatik artsın ve show_employee_count() çalıştırılarak çalışan sayısı ekrana basılsın

# class Department:
# 	"""
# 	Class Documantation
# 	"""
# 	department = 'Software Developer'
# 	employee_count = 0
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		Department.employee_count += 1
# 		self.show_employee_count()
#
# 	def show_employee_count(self):
# 		print(f'Total Employee: {self.employee_count}')
#
# 	def show_info(self):
# 		print(f'Name: {self.name}\nAge: {self.age}\nDepartment: {self.department}')
#
#
# d1 = Department('Burak', 34)
# d1.show_info()
#
# d2 = Department('Hakan', 37)
# d2.department = 'ARGE'
# d2.show_info()

# Software_Developer sınıfı açıyoruz
# first_name, last_name, language, languages => object attribute
# add_new_language() fonksiyonu olsun. aynı anda birden fazla dilde eklenebilsin
# show_info() fonksiyonu olsun
# class Software_Developer:
# 	knowleadge = []
#
# 	def __init__(self, first_name, last_name):
# 		self.first_name = first_name
# 		self.last_name = last_name
#
# 	def show_info(self):
# 		return f'First Name: {self.first_name}\n' \
# 		       f'Last Name: {self.last_name}\n' \
# 		       f'Programing Language: {self.knowleadge}'
#
# 	def add_language(self, lst_language: list):
# 		for language in lst_language:
# 			self.knowleadge.append(language.lstrip())
#
# 	def split_language(self, languages: str) -> list:
# 		return languages.split(',')
#
#
# burak = Software_Developer('Burak', 'Yılmaz')
# language = input('Please type into programming skills: ')
# languages = burak.split_language(language)
# burak.add_language(languages)
# print(burak.show_info())


# Character isminde bir sınıf yaratalım
# Object Attribute => name, race, role, level, weapon armour, hp
# Fonksiyonlar => attack, defend, escape
# saldırırken level + weapon kadar vursun
# savunurken level + armour
# escape olduğunda tapuk yapsın
class Character:
	def __init__(self, name: str, race: str, role: str, level: int, weapon: int, armour: int, hp: int):
		self.hp = hp
		self.armour = armour
		self.name = name
		self.race = race
		self.role = role
		self.level = level
		self.weapon = weapon
	
	def attack(self):
		return self.level + self.weapon
	
	def defend(self):
		return self.level + self.armour
	
	def escape(self):
		print('Escape the fight. Cowered..!')


def main():
	kara_murat = Character('Kara Murat', 'Turk', 'Akıncı', 100, 99, 0, 100)
	gostok = Character('Hain Köpek', 'Bizans', 'Şovalye', 50, 50, 100, 100)
	
	while True:
		action = input('For Attack ==> a\n'
		               'For Defend ==> b\n'
		               'For Escape ==> e\n'
		               'Choose your move: ')
		
		if action == 'e':
			gostok.escape()
			break
		elif action == 'a':
			kara_murat.hp -= gostok.attack() - kara_murat.defend()
			gostok.hp -= kara_murat.attack() - gostok.defend()
			
			print(f'{gostok.name} verdiği hasar ==> {gostok.attack() - kara_murat.defend()}')
			print(f'{kara_murat.name} verdiği hasar ==> {kara_murat.attack() - gostok.defend()}')
			print("========================================")
			print(f"{gostok.name} kalan can ==> {gostok.hp}")
			print(f"{kara_murat.name} kalan can ==> {kara_murat.hp}")
		else:
			print('Please choose valid actin..!')
		
		if kara_murat.hp <= 0 < gostok.hp:
			print(f'{gostok.name} has victor..!')
			break
		elif kara_murat.hp > 0 >= gostok.hp:
			print(f'{kara_murat.name} has vitor..!')
			break
		elif kara_murat.hp <= 0 and gostok.hp <= 0:
			print(f'Bu dünya hiç kimseye kalmaz. Savaşma......!')
			break
			
			
main()