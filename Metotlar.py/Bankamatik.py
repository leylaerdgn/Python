bakiye = 1000

def bakiye_goruntule():
    """Mevcut bakiyeyi görüntüler."""
    global bakiye
    print(f"Mevcut bakiyeniz: {bakiye} TL")

def para_yatir(miktar):
    """Belirtilen miktarı bakiyeye ekler."""
    global bakiye
    #bakiye_goruntule fonksiyonu, mevcut bakiyeyi ekrana yazdırır. Fonksiyon içindeki global bakiye ifadesi, global bakiye değişkenine erişim sağlar ve güncellenmesini sağlar.
    if miktar > 0:
        bakiye += miktar
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {bakiye} TL")
    else:
        print("Geçersiz miktar. Miktar sıfırdan büyük olmalıdır.")

def para_cek(miktar):
    """Belirtilen miktarı bakiyeden çeker."""
    global bakiye
    if miktar > 0:
        if miktar <= bakiye:
            bakiye -= miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {bakiye} TL")
        else:
            print("Yetersiz bakiye.")
    else:
        print("Geçersiz miktar. Miktar sıfırdan büyük olmalıdır.")

def ana_menu():
    """Ana menüyü görüntüler ve kullanıcıdan seçim yapmasını sağlar."""
    while True:
        print("\n--- Bakiye Uygulaması ---")
        print("1. Bakiye Görüntüle")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Çıkış")
        
        secim = input("Seçiminizi yapın (1/2/3/4): ")
        
        if secim == "1":
            bakiye_goruntule()
        elif secim == "2":
            miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
            para_yatir(miktar)
        elif secim == "3":
            miktar = float(input("Çekmek istediğiniz miktarı girin: "))
            para_cek(miktar)
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Ana menüyü başlat
ana_menu()