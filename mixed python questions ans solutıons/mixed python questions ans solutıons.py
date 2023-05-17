
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

4.Soru: Klavyeden girilen 25 adet sayıdan negatif olanların toplamını çift sayıların toplamını 7 ye
 eşit olanların adetini bulup ekrana yazdıran uygulama

sayac=1
negatif_sayi=0
cift_sayi=0
esit=0
while sayac<26:
    sayi=int(input("sayi: "))
    if sayi<0:
        negatif_sayi+=sayi
    if sayi%2==0:
        cift_sayi+=sayi
    if sayi==7:
        esit+=1
    sayac+=1
print(f"negatif sayi toplamı={negatif_sayi}, çift sayiların toplamı={cift_sayi},yediye eşit olanlar ise {esit}tanedir.")


5.Soru: Girilen sayının 5'in kuvveti olup olmadığını bulan program yazınız.olmadı

sayi=int(input("sayi: "))
for i in range(0,sayi):
    if sayi==5**i:
        print(f"5'in {i}. kuvvetidir")
        break
else:
    print("5'in kuvveti değildir")

2.yol;
sayi=int(input("sayi: "))
if sayi % 5 != 0:
    print("hayır")
else:
    while sayi>0:
        if sayi%5==0:
            sayi=sayi/5
            if sayi == 1:
                print("evet")
                break
        else:
           print("hayır")
           break


































