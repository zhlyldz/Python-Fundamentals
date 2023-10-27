

# Method Overriding
# Ata sınıflarımızda bulunan methodların alt sınıflarda var olan yetenekleri üzerine yeni yetenekler ekleme yada var olan yeteneğini geçersiz kılarak ona yeni yetenek aktarma işlemine method overriding denir.

# from enum import Enum
# from socket import gethostname, gethostbyname
# from datetime import datetime
#
#
# class Status(Enum):
# 	Active = 1
# 	Modified = 2
# 	Passive = 3
#
#
# # Ata sınıflar kalıtım verecekleri alt sınıfların ortak özelliklerini barındırırlar. Bu örnekte category ve product gibi iki tane entity olacak. name ve description attribute her iki varlığında ortak özelliği olduğu için BaseEntity yazılabilinir. Lakin price, stock gibi bilgiler BaseEntity yazılamaz çünkü category varlığının price ve stock özellikleri olmaz.
# class BaseEntity:
# 	def __init__(self, Id, create_date, update_date, delete_date, status, ip_address, machine_name, name, description):
# 		self.description = description
# 		self.name = name
# 		self.machine_name = machine_name
# 		self.ip_address = ip_address
# 		self.status = status
# 		self.delete_date = delete_date
# 		self.update_date = update_date
# 		self.create_date = create_date
# 		self.Id = Id
#
# 	def show_info(self):
# 		print(f'Id: {self.Id}\n'
# 		      f'Name: {self.name}\n'
# 		      f'Description: {self.description}\n'
# 		      f'Status: {self.status}\n')
#
#
# # Category varlığının kendine has bir özelliği olmadığı için içerisine birşey yazmıyoruz
# class Category(BaseEntity):
# 	pass
#
#
# class Product(BaseEntity):
# 	def __init__(self, Id, create_date, update_date, delete_date, status, ip_address, machine_name, name, description, stock, price):
# 		super().__init__(Id, create_date, update_date, delete_date, status, ip_address, machine_name, name, description)
# 		self.price = price
# 		self.stock = stock
#
#
# 	def show_info(self):
# 		super().show_info()
# 		print(f'Price: {self.price}')
# 		print(f'Stock: {self.stock}')
#
#
# # Category sınıfı ata sınıftan aldığı özellikleri kullanmaktadır.
# category_1 = Category(1, datetime.now(), "", "", Status.Active, gethostname(), gethostbyname(gethostname()), 'Boxing Gloves', "Best boxing gloves")
# category_1.show_info()
#
#
# product_1 = Product(1, datetime.now(), "", "", Status.Active, gethostname(), gethostbyname(gethostname()), 'Everlast Pro Gloves', 'Best ever', 13, 12)
# product_1.show_info()


# BasePhone ata sınıfı olsun. phone_id, brand, model, price attribute olsun
# show_info(), phone_ring_sound() fonksiyonları olsun. phone_ring_sound() bize 'Genel Telefon Sesi' return etsin
# Samsung => operating_system attribute olsun.  phone_ring_sound() bize 'Samsung telefon sesi' return etsin
# Iphone => camere attribute olsun. phone_ring_sound() bize 'Iphone telefon sesi' return etsin
# Nokia => anten attribute olsun. phone_ring_sound() bize 'Nokia telefon sesi' return etsin
# class BasePhone:
# 	def __init__(self, phone_id: int, brand: str, model: str, price: float):
# 		self.phone_id = phone_id
# 		self.brand = brand
# 		self.model = model
# 		self.price = price
#
# 	def show_info(self) -> None:
# 		print(f'Id: {self.phone_id}\n'
# 		      f'Model: {self.model}\n'
# 		      f'Brand: {self.brand}\n'
# 		      f'Price: {self.price}')
#
# 	def phone_ring_sound(self) -> str:
# 		return f'Genel telefon sesi'
#
#
# class Samsung(BasePhone):
# 	def __init__(self, phone_id: int, brand: str, model: str, price: float, operating_system: str):
# 		super().__init__(phone_id, brand, model, price)
# 		self.operating_system = operating_system
#
# 	def show_info(self) -> None:
# 		super().show_info()
# 		print(f'OS: {self.operating_system}')
#
# 	def phone_ring_sound(self) -> str:
# 		return f'Samsung telefon sesi'
#
#
# class Iphone(BasePhone):
# 	def __init__(self, phone_id: int, brand: str, model: str, price: float, camera: str):
# 		super().__init__(phone_id, brand, model, price)
# 		self.camera = camera
#
# 	def show_info(self) -> None:
# 		super().show_info()
# 		print(f'Camera: {self.camera}')
#
# 	def phone_ring_sound(self) -> str:
# 		return f'Iphone telefon sesi'
#
#
# class Nokia(BasePhone):
# 	def __init__(self, phone_id: int, brand: str, model: str, price: float, anten: str):
# 		super().__init__(phone_id, brand, model, price)
# 		self.anten = anten
#
# 	def show_info(self) -> None:
# 		super().show_info()
# 		print(f'Anten: {self.anten}')
#
# 	def phone_ring_sound(self) -> str:
# 		return f'Nokia telefon sesi'
#
#
# samsung = Samsung(1, 'Samsung', 'S22', 12.3, 'Android')
# samsung.show_info()
# samsung.phone_ring_sound()
#
#
# iphone = Iphone(2, 'Iphone', '14 Pro Max', 34.5, '16mpi')
# iphone.show_info()
# iphone.phone_ring_sound()
#
# nokia = Nokia(3, 'Nokia', '3310', 9.5, '5dbi')
# nokia.show_info()
# nokia.phone_ring_sound()
		

# BaseBill sınıfımız olacak. bill_name, value_add_task, amount attribute. calculate_bill ve create_log fonksiyonlarımız olsun
# log => bill_info.txt dosyasınd tutulacak. bill_name ve total amount
# Su, Elektrik, DogalGaz sınfılarımız olsun
# Elektrik sınıfının kw
# su mill
# doğal gazda m3 özelliği olsun ona göre calculate_bill dizayn

from datetime import datetime

# aşağıdaki dosya açma kodlarını proje bir kez çalıştırıldıktan sonra yoruma alın
# file = open(file='bill_info.txt', mode='w', encoding='utf8')
# file.write('Bill Information')
# file.close()


class BaseBill:
	def __init__(self, bill_name, value_add_task, amount):
		self.amount = amount
		self.value_add_task = value_add_task
		self.bill_name = bill_name
		
	def calculate_bill(self) -> float:
		return self.amount * self.value_add_task
	
	def create_log(self) -> None:
		with open(file='bill_info.txt', mode='a', encoding='utf8') as file:
			file.write(f'{self.bill_name} || Total Amount: {self.calculate_bill()} || Create Date: {datetime.utcnow()}')


class Electricty(BaseBill):
	def __init__(self, bill_name, value_add_task, amount, kw):
		super().__init__(bill_name, value_add_task, amount)
		self.kw = kw
	
	def calculate_bill(self) -> float:
		return super().calculate_bill() * self.kw
		
		
class NatureGas(BaseBill):
	def __init__(self, bill_name, value_add_task, amount, m3):
		super().__init__(bill_name, value_add_task, amount)
		self.m3 = m3

	def calculate_bill(self) -> float:
		return super().calculate_bill() * self.m3


electricty = Electricty('BEDAŞ', 47.8, 478, 90.1)
electricty.create_log()












		
	
	
	
	
	
	
	
	
	
	
	
	
	