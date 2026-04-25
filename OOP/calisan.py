class Calisan:
    zam_orani = 1.05  # Class attribute
    
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.email = f"{ad.lower()}.{soyad.lower()}@sirket.com"
    
    def tam_ad(self):
        return f"{self.ad} {self.soyad}"
    
    def zam_yap(self):
        self.maas = int(self.maas * self.zam_orani)
        return self.maas

class Yazilimci(Calisan):
    zam_orani = 1.10 #Üst sınıftaki zam_oraninı ezdik (override)
    
    def __init__(self, ad, soyad, maas, programlama_dili):
        super().__init__(ad, soyad, maas)
        self.programlama_dili = programlama_dili
    
    def kod_yaz(self):
        return f"{self.tam_ad()} {self.programlama_dili} ile kod yazıyor..."

class Muhasebeci(Calisan):
    zam_orani = 1.07
    
    def __init__(self, ad, soyad, maas, yazilim):
        super().__init__(ad, soyad, maas)
        self.yazilim = yazilim
    
    def rapor_hazirla(self):
        return f"{self.tam_ad()} {self.yazilim} ile rapor hazırlıyor..."

# Kullanım
yazilimci = Yazilimci("Mehmet", "Demir", 15000, "Python")
muhasebeci = Muhasebeci("Ayşe", "Kaya", 12000, "Excel")

print(yazilimci.kod_yaz())
print(f"Zamlı maaş: {yazilimci.zam_yap()} TL")
print(muhasebeci.rapor_hazirla())