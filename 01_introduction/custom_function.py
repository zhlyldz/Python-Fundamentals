# Custom Functions

# Fonksiyon tanımlarken
# def fonksiyon_name():
#   yapılacak işlem kodların
# fonksiyon bir kez tanımlanır

# fonksiyon_name() artık istediğimiz yerde istediğimiz kadar fonksiyonu çağrırak kullanabiliriz.

# Fonksiyonumuzu tanımladık
# def greeting():
# 	print('Hello YZL3402')


# fonsiyonu istediğim yerde istediğim kadar cağırabilirim
# greeting()


# def greeting_person(full_name: str) -> None:
# 	"""
# 	This function greeting first person
# 	:param full_name:  This argumant take string value
#   :return: None
# 	"""
# 	print(f'Merhaba {full_name}')
#
#
# tam_ad = input('Full name: ')
# greeting_person(tam_ad)


# Kullanıcıdan tam adını alım. isim.soyisim@bilgeadam.com mail adresini oluşturarak ekrana basalım
# def mail_creator(full_name: str) -> None:
# 	"""
# 	This function take one argumants and create a mail address with those argumants
# 	:param full_name:  This argumant must be string value
# 	:return: None
# 	"""
# 	name_lst = full_name.lower().split(' ')
# 	print(f'{name_lst[0]}.{name_lst[-1]}@bilgeadam.com')
#
#
# tam_ad = input('Please type your full name: ')
# mail_creator(tam_ad)

# Kullanıcıdan alınan sayı çift mi tek mi olduğunu söyleyen fonksiyonu yazın
# def cif_tek(sayi: int) -> None:
# 	if sayi % 2 == 0:
# 		print(f'{sayi} çifttir..!')
# 	else:
# 		print(f'{sayi} tektir..!')
#
#
# number = int(input('Sayi: '))
# cif_tek(number)
# cif_tek(2)
# cif_tek(12)
# cif_tek(11)


# Kullanıcıdan alınan değerin faktöriyelini hesaplayın
def faktoriyel_hesaplama(x: int) -> None:
	if x < 0:
		print('Sıfırdan küçük sayıların faktoriyeli hesaplanmaz..!')
	else:
		result = 1
		if x == 0 and x == 1:
			print(f'Sonuç: {result}')
		else:
			while x > 1:
				result *= x
				x -= 1
			print(f'Sonuç: {result}')
			
			
faktoriyel_hesaplama(10)
faktoriyel_hesaplama(-12)
faktoriyel_hesaplama(5)
faktoriyel_hesaplama(0)
faktoriyel_hesaplama(1)


# Kullanıcı sign up sonra sign in
# kullanıcı bilgileri dict tutulacak
users_dict = {
	'1': {
		'user_name': 'bear',
		'password': '123'
	},
	'2': {
		'user_name': 'crazy bear',
		'password': '123'
	}
}


def sign_in(user_name: str, password: str) -> None:
	is_true = False
	for i in range(1, len(users_dict) + 1):
		if users_dict.get(str(i)).get('user_name') == user_name and users_dict.get(str(i)).get('password') == password:
			is_true = True
			break
	
	if is_true:
		print('Hoşgeldiniz..!')
	else:
		print('Bilgilerinizi kontrol ediniz..!')
	
	
def get_user_name(user_dict: dict) -> list:
	user_name_lst = []
	
	for i in range(1, len(users_dict) + 1):
		user_name_lst.append(users_dict.get(str(i)).get('user_name'))
		
	return user_name_lst


def sign_up(user_name: str, password: str) -> None:
	if user_name in get_user_name(users_dict):
		print('Farklı bir kullanıcı adı deneyin..!')
	else:
		print('Hesabınız oluşturuldu')
		users_dict[str(len(users_dict) + 1)] = {
			'user_name': user_name, 'password': password
		}
	

def main():
	while True:
		process = input('İşlem giriniz: ').lower()
		if process == 'çıkış':
			break
		elif process == 'giriş yap':
			user_name = input('Kullanıcı Adı: ')
			password = input('Şifre: ')
			sign_in(user_name, password)
		elif process == 'kayıt ol':
			user_name = input('Kullanıcı Adı: ')
			password = input('Şifre: ')
			sign_up(user_name, password)
			print(users_dict)
		else:
			print('Lütfen uygun bir işlem türü giriniz..!')
	
	
main()




