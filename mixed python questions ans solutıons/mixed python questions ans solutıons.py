
Girilen 3 basamaklı bir sayının basamaklarının küpleri toplamı sayının
kendine eşit olup olmadığını bulan programı yazınız.

toplam=0
lst=[]
sayi=input("Sayi: ")
if len(sayi) != 3:
    print("Lütfen 3 basamaklı sayı giriniz")
else:
    for i in sayi:
        lst.append(i)
        toplam+= int(i)**3
    if toplam == int(sayi):
        print(f"Toplamınız sayiya eşittir.")
    else:
        print(f"Toplamınız sayiya eşit değildir.")


Kullanıcıdan alınan 20 adet sayıdan çift sayıların toplamının tek sayıların toplamına oranını bulan uygulamyı bulunuz.
tek_toplam=0
cift_toplam=0
sayac=20
while True:
    if sayac==0:
        break
    sayi=int(input("sayi: "))
    if sayi%2==0:
        tek_toplam+=sayi
    else:
        cift_toplam+=sayi
    sayac-=1
print(cift_toplam/tek_toplam)

tek_toplam=0
cift_toplam=0
sayac=20
while sayac>0:
        sayi=int(input("sayi: "))
        if sayi % 2 == 0:
            tek_toplam += sayi
        else:
            cift_toplam += sayi
        sayac -= 1
print(cift_toplam/tek_toplam)


10 ile 1000 arasındaki tam kare sayıları ekrana yazdıran program yapınız

lst=[]
lst_1=[]

for i in range (10,1000):
    if i**2 in range(10,1000):
        lst_1.append(i**2)
print(lst_1)


































