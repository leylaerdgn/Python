def us_alma(taban,us):
    def hesapla():
        sonuc=1
        for i in range(us):
            sonuc*=taban
        return sonuc
    return hesapla()
taban=int(input("Taban değerini giriniz: "))
us=int(input("Üs değerini giriniz: "))

print(f"{taban} üzeri {us} ={us_alma(taban,us)}")