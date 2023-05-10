Kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulan Python örneği.

sayi_1=int(input("sayi 1: "))
sayi_2=int(input("sayi 2: "))
if sayi_1<sayi_2 and sayi_1>0:
  lst=[]
  for i in range(sayi_1, sayi_2):
      if i %2 == 0:
          lst.append(i)
  print(sum(lst)/len(lst))
else:
  print("Lütfen doğru sayı giriniz")

1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan ve kaç tane olduğunu gösteren uygulama yapınız
list=[]
for i in range(1,101):
     if i%3==0 and i%5==0:
       list.append(i)
       print(i)
print(len(list))


Python ile bir liste içinde 5’in katları olan sayıları listeleme 1-10000

list=[]
for i in range (1,10000):
   if i %5 ==0:
     list.append(i)
print(list)


Bir sayının kendisi dışında bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir.
Kullanıcıdan alınan sayının mükemmel sayı olup olmadığını kontrol eden kodu yazınız.
lst=[]
sayi=int(input("Bir sayı giriniz:"))
for i in range(1, sayi):
    if sayi % i == 0:
        lst.append(i)
if sum(lst) == sayi:
    print(f"{sayi} mükemmel sayıdır")
else:
    print(f"{sayi} mükemmel sayı değildir")

Bir string içerisinde belirlenen bir karakterin olup olmadığını kontrol eden Python programı kodları.

metin=input("metin: ")
for i in metin:
   if i == "k":
    print("karakter vardır")
    break
   else:
       print("Karakter yoktur")
       break

Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir
Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse indirimsiz tutarı#
hesaplayarak ekrana yazdıran kodu yazınız.

aktivite=input("aktivite=")
kisi=input("kisi=")

if aktivite == "sinema":
   if kisi == "öğrenci":
      print(15-15*0.5)
   else:
      print(15)
if aktivite == "tiyatro":
   if kisi=="öğrenci":
      print(10-10*0.5)
   else:
   print(10)

Girilen metnin harflerini alt alta yazdıran Python Örneği

metin=input("metin=")
for i in metin:
   print(i)



