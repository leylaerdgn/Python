#RegEx = metin içinde arama yapma yöntemi
#findall() → hepsini bulur
#search() → ilk eşleşmeyi bulur

import re

print("=== PYTHON REGEX ÖRNEKLERİ ===\n")

txt = "The rain in Spain"

# 1. search() - başlangıç ve bitiş kontrolü
print("1) search (^The...Spain$):")
x = re.search("^The.*Spain$", txt)
print(x)

# 2. findall() - tüm eşleşmeler
print("\n2) findall (ai):")
x = re.findall("ai", txt)
print(x)

# eşleşme yoksa
print("\nfindall (Portugal):")
x = re.findall("Portugal", txt)
print(x)

# 3. search() - ilk boşluk karakteri
print("\n3) search (ilk boşluk):")
x = re.search("\s", txt)
if x:
    print("İlk boşluk pozisyonu:", x.start())

# eşleşme yoksa
print("\nsearch (Portugal):")
x = re.search("Portugal", txt)
print(x)

# 4. split() - boşluklara göre ayırma
print("\n4) split:")
x = re.split("\s", txt)
print(x)

# maxsplit ile
print("\nsplit (1 kez):")
x = re.split("\s", txt, 1)
print(x)

# 5. sub() - değiştirme
print("\n5) sub:")
x = re.sub("\s", "9", txt)
print(x)

# belirli sayıda değiştirme
print("\nsub (2 kez):")
x = re.sub("\s", "9", txt, 2)
print(x)

# 6. metakarakter örneği
print("\n6) Metakarakter (h.*o):")
x = re.findall("h.*o", "hello world")
print(x)

# 7. özel diziler
print("\n7) Özel diziler:")
print("Sayılar:", re.findall("\d", "abc123"))
print("Boşluklar:", re.findall("\s", txt))
print("Kelimeler:", re.findall("\w", txt))

# 8. set kullanımı
print("\n8) Set örnekleri:")
print("[a-m]:", re.findall("[a-m]", txt))
print("[0-9]:", re.findall("[0-9]", "abc123"))
print("[^a]:", re.findall("[^a]", "banana"))

# 9. flag kullanımı (ignore case)
print("\n9) Flag (IGNORECASE):")
x = re.search("python", "PYTHON öğreniyorum", re.IGNORECASE)
print(x)

# 10. Match object kullanımı
print("\n10) Match object:")
x = re.search("ai", txt)
if x:
    print("span:", x.span())
    print("group:", x.group())
    print("string:", x.string)

# 11. S ile başlayan kelime bulma
print("\n11) S ile başlayan kelime:")
x = re.search(r"\bS\w+", txt)
if x:
    print("Bulunan:", x.group())

print("\n=== BİTTİ ===")