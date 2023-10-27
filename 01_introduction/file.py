
# File I/O
# Dosya açmai kapama, var olan dosya üzerine yeni bilgiler yazma silme yani dosya üzerinden CRUD işlemlerini yapmak için python içerisine bulunan File I/O modülünü kullanacağız.

# Dosya açma
file = open(file='new_file.txt', mode='w', encoding='utf-8')
# open() fonksiyonu python içerisinde gömülü (built-in) olarak bulunmaktadır. Bu fonksiyon içerisine aldığı değerleri göz önünde bulundurak bize bir dosya yaratıcak.
# file argümanı dosyaya isim vermemizi temin eder.
# mode argümanı yaratılacak dosyanın amacını belirtmetedir. Biz burada dosya üzerine yazı yazmak isteidiğimiz için 'w' yani writable demek istedik.
# encoding argümanı dosyamıza karakrter desteği vemek için var. Biz burada türkçe karakter desteği verdik.

# Not: open() fonksiyonu çalıştığında dosya şayet önceden açılmışsa bir daha aynı dosyayı yaratmaz. Var olanı kullanır.

file.write('Adı: Burak Yılmaz\nMesleği: Yazılmcı\n')
file.close()

# Aşağıda dosyamıza yeni bir veri girmek istiyoruz ve var olan bilgilerin kaybolmadan bu işlemin geçekleştirmke istiyoruz yani dosyamıza yeni bir veri append etmek istiyoruz. Bu yüzden 'mode' argümanımıza 'a' bilgisi gönderdik.
file = open(file='new_file.txt', mode='a', encoding='utf-8')
file.write('Yazılım Dili: Python\n')
file.close()

# Dosya içerisinde yazan herşeyi okumak istediğimizde "mode" argümanına 'r' yani readable olarak dosyamızı aç diyoruz.
file = open(file='new_file.txt', mode='r', encoding='utf-8')
sentences = file.readlines()
for sentence in sentences:
	print(sentence)
	
	
# Şayet olmayan bir dosyayı açmak istersek
# file_name = input('Enter the name of file you want to open: ')
# file = open(file=file_name, mode='r', encoding='utf-8')
# Yukarıda ki kod bloğu çalıştığında uygulama bize bir exception (istisna) raise etti.
# Traceback (most recent call last):
#   File "C:\Users\burak\Downloads\YZL3402\YZL3402\01_Introduction\Lab_13.py", line 31, in <module>
#     file = open(file=file_name, mode='r', encoding='utf-8')
# FileNotFoundError: [Errno 2] No such file or directory: 'students'
# Burada alınan hata => FileNotFoundError
# Bu tarz alınan hataları geliştirici olarak bizlerin handle etmesi gerekmektedir. Bu işlemede kendi aramızda exception handling diyoruz.
# Bir uygulamanın exception raise etmesi en istenmedik durumdur. Müşteri ile bizi karşı karşıya getirir ve uygulamanın güvenirliliği azaltır.
# Bu istisnai durumları handle edebilmek için python içerisinde "try-except" mekanizması bulunmaktadır.
# Hata beklenen kodları "try" bloğu içerisine beklenilen istisnai durumlarıda "except" bloğuna yazıyoruz.
# Try-Except sayesinde uygulamalar exception raise etmiyor ve hatalar giderilmiş oluyor.
# Şimdi yukarıdaki exception handle edelim.
# try:
# 	file_name = input('Enter the name of file you want to open: ')
# 	file = open(file=file_name, mode='r', encoding='utf-8')
# except FileNotFoundError as ex:  # burada "FileNotFoundError" modülüne burada as aracılığıyla "ex" takma adını verdik.
# 	# Burada kullanıcıya anlamlı bir feedback vermek gerekmektedir. Onun yanıda "ex.__doc__" kodu ise kendimiz için yazdık. Alınan hatanın developer tarafından anlaşılması için.
# 	print(f'File does not found.\n{ex.__doc__}')

# x = 5 / 0
# Yukarıda ki kod çalıştığında
# Traceback (most recent call last):
#   File "C:\Users\burak\Downloads\YZL3402\YZL3402\01_Introduction\Lab_13.py", line 51, in <module>
#     x = 5 / 0
# ZeroDivisionError: division by zero
# try:
# 	x = 5 / 0
# 	print(x)
# except ZeroDivisionError as err:
# 	print(err.__doc__)

# try:
# 	lst = [12, 34, 56]
# 	print(lst[10])
# except:  # burada spesifik bir exception modülü belirtmedik. Bütun exception modüllerini burada kontrol ederek hangi exception geldiyse ona göre hareket edecek.
# 	print(f'Listenin eleman sayısı: {lst.__len__()}')


from random import choice

exceptions = [ValueError, TypeError, IndexError, None]

try:
	random_err = choice(exceptions)
	
	print(f'Random Exception is {random_err} and it type is {type(random_err)}')
	
	if random_err:  # random_err değişkeni dolu ise if bloğu çalışacak zaten boş olma olasılı yok.
		raise random_err('An error happend..!')  # burada "raise" anahtar sözcüğü ile exception biz kendi elimizle tetiklemiş olduk. burada bir exception raise olduğu için uygulama durucak ve "except" bloğuna inecek
except ValueError as err:
	print(f'Caught a value error..!\n{err.__doc__}')
except TypeError as err:
	print(f'Caught a type error..!\n{err.__doc__}')
except IndexError as err:
	print(f'Caught a index error..!\n{err.__doc__}')
else:
	# Herhangi bir exception tetiklenmez ise else bloğu devreye girer
	print('If there is no exception when this code call..!')
finally:
	# finnaly bloğu try boğu başarılı olsada çalışır, exception hediğimizde de çalışır her durum ve koşul aldtında çalışır.
	print('No matter what this block can be call..!')











