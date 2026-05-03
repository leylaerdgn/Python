kisiler=[]
while True:

    kisi=input('Kişi giriniz: ')
    if kisi=='q':
        break
    
    yasi=int(input('Yaşı: '))

    sozlukler={
        "kisi": kisi,
        "yasi": yasi
    }

    kisiler.append(sozlukler)

aranan=input("aranacak isim: ")
bulundu=False

for kisi in kisiler:
    if kisi["kisi"] == aranan:
        print("bulundu")
        print(kisi)
        bulundu=True 
        
if not bulundu:
    print("Bulunamadı.")
