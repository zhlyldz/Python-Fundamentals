# Barbut
# bots = ['bot_1', 'bot_2' ....] =>
# user_dict = {
# 	'1': {
# 		'user_name': '',
# 		'şifre': '',
# 		'safe': 21321321
# 	}
# }
# Kullanıcı login olucak, login olurken daily chip, login olan adamın karşısına random bot gelecek
# kullanıcı uygun bet yapıyor mu yani minimum bahis max kasası kadar
# zar atılacak
# bahis yapıalcak kazanırsa kazana pottakı parayı alacak
# kayıp ederse kasasından düşecek
from random import choice, randint


bots = ['ahmet', 'mehmet', 'ayşe']
minimum_bet = 100
user_dict = {
	'1': {
		'user_name': 'beast',
		'password': '123',
		'safe': 1200
	},
	'2': {
		'user_name': 'keko',
		'password': '123',
		'safe': 2200
	}
}


# Aşağıda ki fonksiyonda bulunna argüman üzerinden bir liste alınır ve bu liste içerisinde bulunna item'lardan bir tanesi random olarak geri döndürülür. Bu işlem için random modülünde bulunan choice() fonksiyonunu kullandık. choice fonksiyonu aşağıda gördüğünüz gibi argüman olarak bir liste beklemektedir. Verilen bu listeden random bir item bize teslim etmektedir.
def assing_defult_bot(lst: list) -> str:
	return choice(lst)


# Bu fonksiyonda random modülüne ait randint() fonksiyonu ile 1-6 arasında bir sayı üretildi. BU fonksiyonu 2 kez kullandık çünkü barbut oyununda iki zar bulunmaktadır ve en büyük atan kişi kazanır. burada her bir randint() fonksiyonu bir zarı temsil etmektedir.
def roll_dicle() -> int:
	return randint(1, 6) + randint(1, 6)


# bet_is_valid() fonksiyonu 2 argüman almaktadır. "bet" argümanı kullanıcını oyun esnasında yaptığı bahisi, "safe" argümanı ise kullanıcının anlık olarak kasasını fonksiyana taşımka için bulunmaktadır. bahis yani "bet" değişkeni oyun içerisinde sabit olarak tanımlanan minimum_bet ile kasa arasında bir değer ise bizim için uygun bir bahistir. Fonksiyonda bunu kontrol edere bize boolean bir değer dönmektedir.
def bet_is_valid(bet: int, safe: int) -> bool:
	if minimum_bet <= bet <= safe:
		return True
	else:
		return False


# Burada ki iş mantığı (business logic) kullanıcı her login olduğunda ona günlük free chip hediye etmektir. Bunun için gene random sayı üreten randint() fonksiyonunu kullandık.
def gain_daily_chips() -> int:
	return randint(1000, 2000)


# Login iş manıtğı için aşağıda ki fonksiyon kullanılmıştır. Bu fonksiyon user_name ve password argümanları almaktadır.
def login(user_name: str, password: str) -> dict:
	is_user_active = False  # burada bir boolean değişken tanımladık login olan kullanıcıyı yakaladığımızda True değeri vereceğiz şayet login olacak kullanıcı bizim veri tabanımızda yoksa başlangıç değeri olan False kalacaktır.
	counter = ''  # burada "counter" isimli bir değişken kullandım. Çünü aşağıda ki loop içerisinde anahtarları temsil eden "i" değerini loop'ın yaşam alanı dışında kullanamazdım. Bu yüzden fonksiyon içerisinde counter isimli bir değişken kullandım.
	# Aşağıda ki döngüde range() fonsiyonu ile 1 - user_dict sözlüğünün eleman sayısı kadar döncek olan bir sayı listesi oluşturduk ve bu listenin her bir elemanını loop iterate etdiyoruz. Burada ki sayılar sözlüğün içerisinde bulunan anahtar değerleri temsil etmektedir. Lakin burada bir sıkıntı bulunmaktadır. Sözlük teki anahtar değerler str tipinde iken bizim "i" değerimiz int değerindedir bu yüzden get() fonksiyonu içerisinde "i" değerini str tipine dönüştürdük. Ayrıca az önce bahsi geçen get() fonksiyonu sözlüğün anahtar değeri üzerinden o anahtara bağlı olan value teslim etmektedir.
	for i in range(1, len(user_dict) + 1):
		if user_dict.get(str(i)).get('user_name') == user_name and \
				user_dict.get(str(i)).get('password') == password:
			is_user_active = True
			counter = str(i)  # if şartından geçen kullanıcının anahtar değerini for loop yaşam alanından dışarıya fırlatmak için kullanıyorum counter değişkenini.
			break
	
	if is_user_active:
		return user_dict.get(counter)  # burada ki mantığım login olmuş kullanıcının tüm bilgilerini kendime return ediyorum ki uygulma içerisinde bu kullanıcının bilgilerinden faydalanabileyim.
	else:
		return {}  # user_name ve password bilgileri bizim sözlükte yoksa boş dict dönüyoruz yani login işlemi başarısız.


def main():
	auth_user = login(input('User Name: '), input('Password: '))
	if auth_user != {}:
		chips = gain_daily_chips()
		print(f'Welcome, gain {chips} daily chips..!')
		auth_user.update({
			'safe': auth_user.get('safe') + chips
		})
		while True:
			if auth_user.get('safe') >= minimum_bet:
				bet = int(input('Please type your bet'))
				if bet_is_valid(bet, auth_user.get('safe')):
					player_2 = assing_defult_bot(bots)
					
					player_1_roll = roll_dicle()
					player_2_roll = roll_dicle()
					
					print(f"{auth_user.get('user_name')} roller ==> {player_1_roll}")
					print(f"{player_2} roller ==> {player_2_roll}")
					
					if player_1_roll > player_2_roll:
						print(f"{auth_user.get('user_name')} has been victor..!")
						auth_user.update({
							'safe': auth_user.get('safe') + bet ** 2
						})
					elif player_1_roll < player_2_roll:
						print(f"{player_2} has been victor..!")
						auth_user.update({
							'safe': auth_user.get('safe') - bet
						})
					else:
						print('Player tie..!')
				else:
					print("Safe is not vaild.")
			else:
				print("Your bet hasn't been valid..!")
	else:
		print('Kullanıcı bilgilerinizi kontrol ediniz..!')


main()