sayilar=[1,3,5,7,9,12,19,21]
#1 Sayilar listesini while ile yazın.
#  i=0
#   while(i<len(sayilar)):
#   print(sayilar[i])   
#   i+=1

#2 Başlangıç ve bitiş degerlerini kullanıcıdan alıp aradaki tum tek sayıları ekrena yazınız
#baslangic=int(input('İlk sayı: '))
#son=int(input('Son sayı: '))
#i=baslangic
# while(i<son):
#  if(i%2==1):
#   print(f'{baslangic}-{son} arasındaki tek sayılar: {i}')
#  i+=1

#3 Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın
#numbers=[] 
#i=0
#while i < 5:
# sayi=int(input('Sayı: '))
# numbers.append(sayi)
# i+=1
#numbers.sort()
#print(numbers)

#4 Kullanıcıdan alacagınız sınırsız ürün bilgisini ürünler listesi içinde saklayın
#-ürün sayısını kullanıcıya sorun
#-dictionary listesinin yapısı (name,price) şeklinde olsun
#-Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin 
urunler=[]
adet=int(input('Kaç ürün eklemek istiyorsunuz: '))
i=0
while(i<adet):
    name=input('Ürün ismi: ')
    price=input('Ürün fiyatı: ')
    urunler.append({
    'name': name,
    'price': price
    })
    i+=1
for urun in urunler:
 print(f"Ürün adı: {urun['name']} Ürün fiyatı: {urun['price']}")