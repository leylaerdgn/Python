import os

print("=== OS MODÜLÜ ÖRNEKLERİ ===\n")

# 1. os hakkında bilgi
print("1) os modülü içeriği (ilk 10):")
print(dir(os)[:10])

# 2. işletim sistemi adı
print("\n2) İşletim sistemi:", os.name)

# 3. mevcut dizini öğrenme
print("\n3) Mevcut dizin:")
print(os.getcwd())

# 4. klasör oluşturma
print("\n4) Klasör oluşturma:")
if not os.path.exists("newdirectory"):
    os.mkdir("newdirectory")
    print("newdirectory oluşturuldu")

# alt klasör oluşturma
if not os.path.exists("newdirectory/yeniklasor"):
    os.makedirs("newdirectory/yeniklasor")
    print("Alt klasör oluşturuldu")

# 5. dizin listeleme
print("\n5) Bulunduğun klasördeki dosyalar:")
for dosya in os.listdir():
    print(dosya)

# sadece .py dosyaları filtreleme
print("\nSadece .py dosyaları:")
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)

# 6. dosya hakkında bilgi (kendi dosyamızı kontrol edelim)
dosya_adi = __file__
print("\n6) Dosya bilgisi:")
print(os.stat(dosya_adi))

# 7. dosya yolu işlemleri
print("\n7) Dosya yolu işlemleri:")
print("Tam yol:", os.path.abspath(dosya_adi))
print("Klasör yolu:", os.path.dirname(os.path.abspath(dosya_adi)))

# 8. dosya var mı?
print("\n8) Dosya var mı?")
print(os.path.exists(dosya_adi))

# 9. dosya mı klasör mü?
print("\n9) Tür kontrolü:")
print("Dosya mı?", os.path.isfile(dosya_adi))
print("Klasör mü?", os.path.isdir(dosya_adi))

# 10. path birleştirme
print("\n10) Path birleştirme:")
print(os.path.join("C:\\", "deneme", "deneme1"))

# 11. klasör ismini değiştirme
print("\n11) Klasör yeniden adlandırma:")
if os.path.exists("newdirectory") and not os.path.exists("yeniklasor"):
    os.rename("newdirectory", "yeniklasor")
    print("newdirectory -> yeniklasor olarak değiştirildi")

# 12. klasör silme (boş olmak zorunda!)
print("\n12) Klasör silme:")
if os.path.exists("yeniklasor/yeniklasor"):
    os.rmdir("yeniklasor/yeniklasor")  # önce iç klasör silinir

if os.path.exists("yeniklasor"):
    os.rmdir("yeniklasor")
    print("Klasörler silindi")

