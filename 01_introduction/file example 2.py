
# Bu çalışmada, bir uygulamada alınan hataları not defterine kayıt edilmesi yapıalcaktır.
# Bu işleme bizim sektörde log tutma denir. Log bir uygulamada neler yapılmış, hangi kullanıcı ne nane yemiş, hangi hata alınmış bunları tutuğumuz bir yapıdır. Log hayat kurtatır.
# Örneğin bir IK çalışanı, kimi görüntülemiş, hangi personeli update etmiş yada silmiş bu işleri hangi bilgisayarda yapmış ne zaman yapmış gibi bilgileri tutarız.
# Bunun yanında uygulamanın arka tarafra işlemleri yaparken raise ettiği exceptionları da kayıt altına alırız. Böylelikle uygulamanın bakım onarımı yapılır (maintance)

# Bu çalışmada alınan exceptionları basit bir kriptografi algoritması ile kriptolayarak log.txt dosyaısna yazacağız.

from socket import gethostname, gethostbyname
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

machine_name = gethostname()
ip_address = gethostbyname(machine_name)
error_date = datetime.utcnow()

try:
	file = open(file='log.txt', mode='w', encoding='utf-8')
	file.write('Application Exception Logs\n')
	file.close()
	try:
		age = int(input('Please type into age: '))
		print(f'Your age is {age}')
	except ValueError as err:
		key = get_random_bytes(16)
		obj = AES.new(key, AES.MODE_CBC)
		chipper_text = obj.encrypt(b'valueerrorhappen')
		file = open(file='log.txt', mode='a', encoding='utf-8')
		file.write(str(chipper_text))
		file.write(" || ")
		file.write(f'Machine Name: {machine_name}')
		file.write(" || ")
		file.write(f'Ip Address: {ip_address}')
		file.write(" || ")
		file.write(f'Error Time: {error_date}')
		print("Age information haven't any character..!")
except IOError as err:
	print(f'{err.__doc__}')
	