

# Encapsulation (Veri Gizleme)
# Bir sınıfın her hangi bir üyesini encapsulation ettiğimiz zaman, ilgili üyeye alt sınıflardan erişemeyiz böylelikle bu üyeyi erişime kapamış oluyoruz. Yani enkapsüle edişmiş bir üye alt sınıflarda değiştirilemeyecektir. Buna bir nevi sınıf dışında erişime yani müdaheleye kapatmka diyebiliriz. Belirli şartlart doğrultusunda bu erişimi dolaylı yollar ile yapabiliyoruz.

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint


class Status(Enum):
	Active = 1
	Modified = 2
	Passive = 3
	
	
class BaseEntity:
	# Encapsule edilecek attribute'lere dışarıdan gelecek değerler atanmaz. Çünkü dış erişime kapatıyoruz.
	# encapsulation edilecek üyelerin başına double under score koyuyoruz.
	def __init__(self):
		self.__id = ''
		self.__create_date = ''
		self.__created_computer_name = ''
		self.__created_ip_address = ''
		self.__status = ''
		
	# BaseEntity sınıfından instance alarak bir obje oluşturduğumuzda, obje üzerinden yukarıdaki herhangi bir attribute erişemedik.

	def set_value_private_attribute(self):
		self.__id = uuid4()
		self.__create_date = datetime.utcnow()
		self.__created_computer_name = gethostname()
		self.__created_ip_address = gethostbyname(gethostname())
		self.__status = Status.Active.name
	

	def show_information(self):
		return self.__dict__
	
	
# b1 = BaseEntity()
# b1.set_value_private_attribute()
# pprint(b1.show_information())

class Product(BaseEntity):
	def __init__(self, name, description):
		super().__init__()
		self.description = description
		self.name = name
		self.__price = 0
		self.__stock = 0
		
	def set_value_product_attribute(self, price, stock):
		super(Product, self).set_value_private_attribute()
		if price >= 0 and stock >= 0:
			self.__price = price
			self.__stock = stock
			print('Product has been created!')
			pprint(self.__dict__)
		else:
			print('Invalid input!\nProducts stock and price can not negative value or zero!')


name = input('Product Name: ')
description = input('Description: ')
price = float(input('Price: '))
stock = int(input('Stock: '))

p1 = Product(name, description)
p1.set_value_product_attribute(price, stock)







	
	

	
	
	
	
	
	
	
	