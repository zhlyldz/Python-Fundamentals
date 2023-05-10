Example-1
ismi Çağrı soyismi Güngör doğum tarihi 1992 doğum yeri Ankara yaşadığı yer Odessa  olan birinin bilgilerinden bir cümle
oluşturma

isim="Çağrı"
soy_isim="Güngör"
dogum_tarihi=1992
dogum_yeri="Ankara"
yasadigi_yer="Odessa"
print(f"{isim} {soy_isim} {dogum_tarihi} tarihinde {dogum_yeri}da doğmustur. Şuan {yasadigi_yer}'da yaşamaktadır.")

input ile girilen bir ismin büyük ünlü uyumuna uyup uymadığını kontrol eden bir program yazınız

isim=input("isim: ")
sesli_harf=["a","ı","o","u","e","i","ö","ü"]
kalin_unlu=["a","ı","o","u"]
ince_unlu=["e","i","ö","ü"]
x=0
y=0
for harf in isim:
    if harf in kalin_unlu:
        x+=1
    elif harf in ince_unlu:
        y+=1
if x == 0 or y == 0:
    print("Büyük ünlü uyumu ile uyumlu")
else:
    print("Büyük ünlü uyumu ile uyumsuz")

kullanıcı adının admin sifrenin TC1923 olduğu bir sifreyi kontrol eden şifre doğruysa sifre basarılı değilse sifre
basarısız yazan ve sifreyi tekrar soran bir program yazınız

kullanici_adi=input("isim: ")

if kullanici_adi== "admin":
    while True:
        sifre = input("sifre: ")
        if sifre == "TC1923":
            print("Başarılı..!")
            break
        else:
            print("Başarısız...! Şifreniz yanlış")
else:
    print("Başarısız..! Kullanıcı adınız yanlış")



























