sayilar = []
toplam=0
sayiAdedi=0
while True:
    sayi= int(input('Sayı giriniz: '))

    if sayi==0:
        break
    elif sayi<0:
        print('Negatif sayı kabul edilemez.')
        continue
    else:
        sayilar.append(sayi)
        toplam+=sayi
        sayiAdedi+=1

print('Sayilarin listesi' ,sayilar)
print('Sayıların toplamı: ',toplam)
print('Girilen sayı adedi: ', sayiAdedi)
print(max(sayilar))
print(min(sayilar))