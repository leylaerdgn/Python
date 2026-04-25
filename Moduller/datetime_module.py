#Python’da tarih için özel bir veri tipi yoktur
#Bunun yerine datetime modülü kullanılır

import datetime
# 1. Şu anki tarih ve saat
x = datetime.datetime.now()
print("Şu an:", x)

# 2. Yıl ve gün adı
print("Yıl:", x.year)
print("Gün adı:", x.strftime("%A"))

# 3. Belirli bir tarih oluşturma
tarih = datetime.datetime(2018, 6, 1)
print("Oluşturulan tarih:", tarih)

#strftime(): Tarihi okunabilir stringe çevirir. Formatı sen belirlersin
print("Ay adı:", tarih.strftime("%B"))


# 5. Farklı format örnekleri
print("\n--- FORMAT ÖRNEKLERİ ---")
print("Kısa gün adı:", x.strftime("%a"))
print("Tam gün adı:", x.strftime("%A"))
print("Gün numarası:", x.strftime("%d"))
print("Ay (sayı):", x.strftime("%m"))
print("Ay (isim):", x.strftime("%B"))
print("Yıl:", x.strftime("%Y"))
print("Saat (24):", x.strftime("%H"))
print("Saat (12):", x.strftime("%I"))
print("AM/PM:", x.strftime("%p"))
print("Dakika:", x.strftime("%M"))
print("Saniye:", x.strftime("%S"))
print("Tarih + saat:", x.strftime("%c"))