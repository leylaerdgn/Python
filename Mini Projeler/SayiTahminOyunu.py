bakiye=1000

print('Yapacağınız işlemi seçiniz:\n1- Bakiye Görüntüle\n2- Para Yatır\n3- Para Çek\n4- Çıkış')

while True:
    islem=int(input('Seçiminiz: '))

    if islem==1:
        print(bakiye)
    elif islem==2:
        miktar=int(input('Ne kadar yatırmak istiyorsunuz: '))
        bakiye+=miktar
        print(bakiye)
    elif islem==3:
        miktar=int(input('Ne kadar çekmek istiyorsunuz: '))
        if bakiye>miktar:
            bakiye-=miktar
            print(bakiye)
        else:
            print('Yetersiz bakiye')
    elif islem==4:
        exit()

