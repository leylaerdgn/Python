# DOSYA İŞLEMLERİ - TÜM ÖRNEKLER

import os

dosya_adi = "demofile.txt"

# 1. Dosya oluşturma ve başlangıç yazma (w varsa siler)
with open(dosya_adi, "w") as f:
    f.write("Hello! Welcome to demofile.txt\n")
    f.write("This file is for testing purposes.\n")
    f.write("Good Luck!\n")

print("1) Dosya oluşturuldu ve içerik yazıldı.\n")

# 2. Dosyayı tamamen okuma
with open(dosya_adi, "r") as f:
    print("2) Tüm içerik:")
    print(f.read())

# 3. İlk 10 karakteri okuma
with open(dosya_adi, "r") as f:
    print("\n3) İlk 10 karakter:")
    print(f.read(10))

# 4. Satır satır okuma
print("\n4) Satır satır okuma:")
with open(dosya_adi, "r") as f:
    for line in f:
        print(line.strip())

# 5. Dosyaya ekleme yapma (a)
with open(dosya_adi, "a") as f:
    f.write("\nYeni bir satır eklendi.")

print("\n5) Dosyaya yeni satır eklendi.")

# 6. Listeyi dosyaya yazma (w ile üzerine yazar)
isimler = ["Ali", "Ayşe", "Mehmet"]
with open("isimler.txt", "w") as f:
    for isim in isimler:
        f.write(isim + "\n")

print("6) isimler.txt oluşturuldu.")

# 7. Dosyada kelime arama
with open(dosya_adi, "r") as f:
    icerik = f.read()
    if "Python" in icerik:
        print("\n7) 'Python' kelimesi bulundu!")
    else:
        print("\n7) 'Python' kelimesi bulunamadı.")

# 8. Satır sayısını bulma
with open(dosya_adi, "r") as f:
    satir_sayisi = len(f.readlines())
    print(f"\n8) Satır sayısı: {satir_sayisi}")

# 9. Dosya kopyalama
with open(dosya_adi, "r") as f1:
    veri = f1.read()

with open("kopya.txt", "w") as f2:
    f2.write(veri)

print("9) Dosya kopyalandı (kopya.txt).")

# 10. Dosya silme
silinecek_dosya = "kopya.txt"

if os.path.exists(silinecek_dosya):
    os.remove(silinecek_dosya)
    print(f"10) {silinecek_dosya} silindi.")
else:
    print("10) Dosya bulunamadı.")