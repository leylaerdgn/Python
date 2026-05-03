ogrenciler ={}

toplam=0
adet=0

while True:
    isim=input("İsim (çıkmak için q): ")

    if isim=="q":
        break
    notu=int(input("Not: "))

    ogrenciler[isim] = notu
    toplam+=notu
    adet+=1

if adet>0:
    ortalama=toplam/adet
    print("Ortalama: " ,ortalama)
else:
    print("Hiç öğrenci girilmedi")

print("Öğrenciler: ",ogrenciler)