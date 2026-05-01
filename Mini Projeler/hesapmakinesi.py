#basit hesap makinesi +kullanıcı bilgisi
isim=input('isminiz: ')
print(f'Merhaba {isim}, hesap makinesine hoş geldin!')

yas= int(input('Yaşınız: '))
if(yas<=18):
    print('BU programı kullanabilmek için 18 yaş ustu olmalısın!')
    exit()

print('Hangi işlemi yapmak istiyorsunuz? \n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme  ')

islem=input('')

print('iki sayı giriniz: ')
sayi1=input('sayı1: ')
sayi2=input('sayı2: ')

sayi1=int(sayi1)
sayi2=int(sayi2)

if(islem=='1'):
   topla=sayi1+sayi2
   print(topla)

elif(islem=='2'):
    cikarma=sayi1-sayi2
    print(cikarma)
elif(islem=='3'):
    carpma=sayi1*sayi2
    print(carpma)
else:
    bolme=sayi1/sayi2
    print(bolme)




