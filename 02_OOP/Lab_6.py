
# Soyutlama (Abstraction)
# OOP yapıları içerisinde en önemlisidir.
# Üst seviyeli yazımlım prebsiplerine (SOLID) uymka istiyorsak ilk adım soyutlama.
# Tasarım desenleri içerisinde soyutlama yoğun olarak kullanılmaktadır.

# Soyutlamaya geçmeden önce öğrenmemiz gereken bir konu bulunmakradır.

# DECORATOR
# Python'da kullanılan bir keyword. Bir fonksiyonu bir decorator ile onun var olan yeteneği üzerine bir yetenek daha eklenir. Yani adı üzerinde ilgili fonksiyonu dekore etmiş oluyoruz. Python gibi güçlü bir dilde built-in decorator'ler bulunmaktadır. Bizde custom decorator yazabiliriz.

# def uppercase_name(function):
# 	def inner_func():
# 		func = function()
# 		make_uppercase = func.upper()
# 		return make_uppercase
#
# 	return inner_func()
#
#
# def get_fullname():
# 	return 'mike tyson'
#
#
#
# print(uppercase_name(get_fullname))
#
#
# @uppercase_name
# def get_name():
# 	return 'burak yılmaz'
#
#
# print(get_name)

# from math import pow, factorial
# from time import sleep, time
#
#
# def calculate_time(func):
# 	def inner_func(*args, **kwargs):
# 		start_process = time()
# 		sleep(5)
# 		func(*args, **kwargs)
# 		finis_process = time()
# 		print(f'================\n'
# 		      f'Process Name: {func.__name__}\n'
# 		      f'Start Time: {start_process}\n'
# 		      f'End: {finis_process}\n'
# 		      f'=================')
#
# 	return inner_func
#
#
# @calculate_time
# def us_alma(a: int, b: int):
# 	print(f'Sonuc: {pow(a, b)}')
#
#
# @calculate_time
# def faktoriyel_hesplama(number: int):
# 	print(f'Sonuç: {factorial(number)}')
#
#
# @calculate_time
# def toplama(x: int, y: int, z: int):
# 	print(f'Sonuç: {x + y + z}')
#
#
# us_alma(2, 3)
# faktoriyel_hesplama(5)
# toplama(1, 2, 3)

from abc import ABC, abstractmethod


# Ata entity sınıfını oluştutuyorum
class BaseMuzikAleti:
	def __init__(self, brand, model):
		self.model = model
		self.brand = brand


class Gitar(BaseMuzikAleti):
	def __init__(self, brand, model, tel):
		super().__init__(brand, model)
		self.tel = tel


class Keman(BaseMuzikAleti):
	def __init__(self, brand, model, kasa):
		super().__init__(brand, model)
		self.kasa = kasa


class Muzisyen:
	def __init__(self, first_name, last_name):
		self.last_name = last_name
		self.first_name = first_name
		self.caldigi_enstruman = []
		
		
# Service mantığı bir varlığın (entity) CRUD operasyonlarını yürütürken ihtiyaç duyulan fonksiyonları barındıran yerdir.
# ABC sınıfı aslında bir meta class'dır. ABC built-in bir meta sınıftır. Biz custom meta sınıflar yazabililiriz.
# Bütün ata sınıflar üst seviyeli yazılım prensiplerine uymak istiyorsak soyut olmalıdır. entity sınıflarım hariç tutulabilinir.
class BaseService(ABC):
	# Abstract bir sınıfın aşağıda ki gibi abstract üyesine (member) gövde yazılmaz. Çünkü bu üye alt sınıflarda kullanılmak zorundadır. Zaten ezip (override) ona alt sınıfta yetenek kazandıracaksam neden burada bir iş ona yükleyeyim. Bu yüzde abstract methodların gövdesi olmaz.
	@abstractmethod
	def call_sound(self) -> str:
		pass
	# Burada ki mekanizma ile alt sınıf ile üst sınıf arasında sözleşme imzalamış oluyoruz yani üst sınıftan kural koymuş oluyoruz. Alt sınıf koyduğumuz kurala uymak zorundadır. Uymazsa instance alarak onu kullanamayız.

	# Abstract bir sınıf içerisinde abstract olmayan üye barındırılabilinir. BUnun mantığıda bazı iş mantıkları alt sınıflarda değiştirilmeden kullanılabilinir. Her method yada fonksiyon değiştirilecek diye bir kaide bulunmamaktadır.
	# Bu methodu bazı sınıflarda kullanabilirim bazı alt sınıflarda kullanamaya bilirim. call_sound() gibi her sınıfta kullanmka zorunda değilim.
	def hello_everyone(self):
		print('Hi...!')
	
	
class GitarService(BaseService):
	def call_sound(self) -> str:
		return 'gitar sesi'

	def hello_everyone(self):
		print('Salve..!')
		

class KemanService(BaseService):
	def call_sound(self) -> str:
		return 'keman sesi'
	
	# static method ve instance method
	@staticmethod
	def harmonize():
		print('Akor edildi..!')
	
	
def main():
	gitar_service = GitarService()
	keman_service = KemanService()
	
	gitar = Gitar('Fender', 'Classical Gitar', 'Kaliteli tel')
	keman = Keman('Sevilla', 'Classical', 'Meşe')
	
	muzisyen = Muzisyen('burak', 'yılmaz')
	muzisyen.caldigi_enstruman.append(gitar)
	muzisyen.caldigi_enstruman.append(keman)
	
	print(f'Ad: {muzisyen.first_name}\n'
	      f'Soyad: {muzisyen.last_name}\n'
	      f'Çaldığı Enstrüman Adı: {muzisyen.caldigi_enstruman[0].brand}\n'
	      f'Çaldığı Enstrüman Model: {muzisyen.caldigi_enstruman[0].model}\n'
	      f'Çaldığı Enstrüman Sesi: {gitar_service.call_sound()}')
	
	print(f'Ad: {muzisyen.first_name}\n'
	      f'Soyad: {muzisyen.last_name}\n'
	      f'Çaldığı Enstrüman Adı: {muzisyen.caldigi_enstruman[1].brand}\n'
	      f'Çaldığı Enstrüman Model: {muzisyen.caldigi_enstruman[1].model}\n'
	      f'Çaldığı Enstrüman Sesi: {keman_service.call_sound()}')
	
	KemanService.harmonize()
	
	
main()









