
# BaseEntity sınıfı oluşturun. öğrendiğimi tüm yapılar olsun.
# Role enum olsun. Admin, Member
# User adında bir sınıfım olsun. Attribute => first_name, last_name, password, role. create edilen user'in rolü otomatik olarak member olacak.
# UserBusinessLogic sınıfım olsun. Bu sınıf içerisinde user varlığının CRUD operasyonları yapılsın.
# isteyen CRUD operasyonunu not defterinde, dictionary yada liste de tutabilir.
from enum import Enum
from datetime import datetime
from socket import gethostname, gethostbyname
from uuid import uuid4
from pprint import pprint

# Bir kere çalıştıktan sonra yoruma almayı unutma
# file = open(file='user_db.txt', mode='a', encoding='utf8')
# file.write('User Database\n')
# file.close()


class Status(Enum):
	Active = 1
	Modified = 2
	Passive = 3
	
	
class Role(Enum):
	Admin = 1
	Memeber = 2


class BaseEntity:
	def __init__(self):
		self.__id = ''
		self.__status = ''
		self.__create_date = ''
		self.__created_machine_name = ''
		self.__created_ip_address = ''
		
		self.modified_date = ''
		self.modified_machine_name = ''
		self.modified_ip_address = ''
		
		self.passived_date = ''
		self.passived_machine_name = ''
		self.passived_ip_address = ''
		
	def set_attribute_base(self):
		self.__id = uuid4()
		self.__create_date = datetime.now()
		self.__created_machine_name = gethostname()
		self.__created_ip_address = gethostbyname(gethostname())
		self.__status = Status.Active.name
		
		
	def show_information(self):
		pprint(self.__dict__)
		

class User(BaseEntity):
	def __init__(self, first_name, last_name, user_name, password):
		super().__init__()
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.password = password
		self.__role = ''
		self.set_attribute_user()
		
	def set_attribute_user(self):
		super().set_attribute_base()
		self.__role = Role.Memeber.name
		
		
	def show_information(self):
		pprint(self.__dict__)
		
		
		
class UserBusinessLogic:
	def create_user(self, first_name, last_name, user_name, password):
		
		user = User(first_name, last_name, user_name, password)
		
		with open(file='user_db.txt', mode='a', encoding='utf8') as file:
			file.write(f'{str(user.__dict__)}\n')
		
		
	def update_user(self):
		pass
	
	def delete_user(self):
		pass
	
	def get_all_user(self):
		pass
	
	def get_by_user_name(self):
		pass
	
	def get_by_id(self):
		pass
		
		
def main():
	user_logic = UserBusinessLogic()
	try:
		user_logic.create_user('Burak', 'Yılmaz', 'beast', '123')
	except TypeError as err:
		print(f'{err.__doc__}')
	except IOError as err:
		print(f'{err.__doc__}')
	
	
main()