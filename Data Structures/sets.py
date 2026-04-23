#Bir küme, sıralanmamış , değiştirilemez* ve indekslenmemiş bir koleksiyondur .
#Sabit öğeler değiştirilemez, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.

def kume_ornek():
    thisset = {"apple", "banana", "cherry"}
    print(thisset)


#ÖGELERE ERİŞİM
#Ancak, bir döngü kullanarak küme öğeleri arasında gezinebilir for veya 
#anahtar kelimeyi kullanarak belirli bir değerin kümede olup olmadığını sorgulayabilirsiniz in.

#Kümede eleman var mı kontrol edelim:
def elememan_varmi():
    thisset = {"apple", "banana", "cherry"}
    print("banana" in thisset)


#update(): Başka bir kümedeki öğeleri mevcut kümeye eklemek için bu update() yöntemi kullan.
#yeni bir küme döndürmez.
def update():
    thisset = {"apple", "banana", "cherry"}
    tropical = {"pineapple", "mango", "papaya"}
    thisset.update(tropical)
    print(thisset)


'''
Birleştirme Kümeleri
Python'da iki veya daha fazla kümeyi birleştirmenin çeşitli yolları vardır.

" union()Ve update()" yöntemi, her iki kümedeki tüm öğeleri birleştirir.

Bu intersection()yöntem yalnızca yinelenen kayıtları saklar.

Bu difference()yöntem, ilk kümedeki öğelerden diğer kümelerde bulunmayanları saklar.

Bu symmetric_difference()yöntem, yinelenenler hariç tüm öğeleri saklar.
'''

#KÜMELEME METOTLARI
'''
add()        → eleman ekler
clear()      → tümünü siler
copy()       → kopya alır

difference() (-)   → farkını alır
difference_update() (-=) → ortakları siler

discard()    → elemanı siler (hata vermez)
remove()     → elemanı siler (yoksa hata verir)
pop()        → rastgele eleman siler

intersection() (&)  → kesişim
intersection_update() (&=) → kesişim dışını siler

isdisjoint() → ortak var mı?
issubset() (<=,<)  → alt küme mi?
issuperset() (>=,>) → üst küme mi?

symmetric_difference() (^)   → farklı olanlar
symmetric_difference_update() (^=) → farklıları günceller

union() (|)   → birleşim
update() (|=) → birleşimle günceller

'''