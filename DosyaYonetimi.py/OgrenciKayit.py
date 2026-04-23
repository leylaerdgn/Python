def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')

    ogrenciAdi=liste[0]
    notlar=liste[1].split(',')

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ort=(not1+not2+not3)/3

if ort >=90 and ort<=100:
    harf='AA'
elif ort >=85 and ort<=89:
   harf='BA'
elif ort >=80 and ort<=84:
   harf='BB'
elif ort >=75 and ort<=79:
   harf='CB'
elif ort >=70 and ort<=74:
   harf='CC'
else:
   harf='FF'

return ogrenciAdi + ": " + harf + "\n"

def ortalamalari_oku():
   with open("sinav_notlari.txt","r",encoding="utf-8") as file:
      for satir in life:
         print(not_hesapla(satir))
        
def not_gir():
   ad=input('Ad: ')
   soyad=input('Soyad: ')
   not1=input('Not 1: ')
   not2=input('Not 2:')
   not3=input('Not 3: ')

   with open("sinav_notlari.txt","a",encoding="utf-8") as file:
      file.write(ad+ " "+soyad+": "+not1+","+not2+","+not3+"\n")

def notlari_kayitet():
   with open("sinav_notlari.txt","r",encoding="utf-8") as file:
      liste=[]
      for i in file:
         liste.append(not_hesapla(i))
         with open("sonuclar.txt","w",encoding="utf-8") as file: 
            for i in liste:
               file3.write(i)