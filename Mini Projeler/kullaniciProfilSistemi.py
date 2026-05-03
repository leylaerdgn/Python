def bilgiler(isim, yas, sehir):
    bilgi = {
        "isim": isim,
        "yas": yas,
        "sehir": sehir
    }
    return bilgi

isim = input('İsminiz: ')
yas = int(input('Yaşınız: '))
sehir = input('Şehriniz: ')

kategori = lambda yas: "çocuk" if yas < 18 else "yetişkin" if yas < 65 else "yaşlı"

kisi = bilgiler(isim, yas, sehir)

print("İsim:", kisi["isim"])
print("Yaş:", kisi["yas"])
print("Şehir:", kisi["sehir"])
print("Kategori:", kategori(yas))