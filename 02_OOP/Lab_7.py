
# Dünyanın farklı lokasyonlarından kahve çekirdeği ithal edeceğiz
# Lakin kahve çekirkelerinin lezzeti ve kalitesi açısından hasat zamanları göz önünde bulundurularak ital edilmesi gerekmektedir.
# 4-11 aylar arasında Columbia'dan ithal edilecek
# 1 yada 2 yada 12. ayda African
# 3. ayda ise hasat zamanı bulunmadığı için herhangi bir yerden ithal edilmeyecek

from abc import ABC, abstractmethod


# Soyut sınıfınların amacı kalıtım vermektir yani onlardan instance çıkartılmaz
class BaseService(ABC):
	@abstractmethod
	def ship_from(self):
		pass
	
	
class SumatraService(BaseService):
	def ship_from(self):
		return 'from Samutra'
	
	
class ColumbiaService(BaseService):
	def ship_from(self):
		return 'from Columbia'


class SouthAfricaService(BaseService):
	def ship_from(self):
		return 'from South Africa'
	
	
class DefaultService(BaseService):
	def ship_from(self):
		return 'shipment not avaliable'
	

# Şiiiiii çaktırma Shipment sınıfı içerisinde ki methodta factory desing pattern kullandım :D :D
# Ne yaptık fabrika kurduk değişik senaryolara göre üretim yaptık yani nesne ürettik değil mi?
class Shipment:
	@staticmethod
	def shipment_method(month) -> BaseService:
		if 4 <= month <= 7:
			return ColumbiaService()
		elif 8 <= month <= 11:
			return SumatraService()
		else:
			if month == 1 or month == 2 or month == 12:
				return SouthAfricaService()
			else:
				return DefaultService()
			
			
def main():
	for month in range(1, 13):
		product_shipment = Shipment.shipment_method(month)
		print(f'Coffee beans shipment {product_shipment.ship_from()}')
	
	
main()