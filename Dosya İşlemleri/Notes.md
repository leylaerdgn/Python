Python’da dosyalarla çalışmak için open() fonksiyonu kullanılır.
open(dosya_adı, mod) şeklinde yazılır.

Modlar:
"r" → Okuma (varsayılan, dosya yoksa hata verir)
"a" → Dosyanın sonuna ekleme yapar (yoksa oluşturur)
"w" → Dosyayı sıfırlayıp yazar (yoksa oluşturur)
"x" → Yeni dosya oluşturur (varsa hata verir)

Ek modlar:
"t" → Metin modu (varsayılan)
"b" → İkili (binary) modu (resim vb.)

with open(...) as f: kullanırsan:
Dosya otomatik kapanır
Daha güvenli ve temizdir

read() → tamamını okur
read(n) → n karakter okur
readline() → 1 satır okur

Bir dosyayı silmek için, işletim sistemi modülünü içe aktarmanız ve işlevini çalıştırmanız gerekir 
os.remove() kullanılır.