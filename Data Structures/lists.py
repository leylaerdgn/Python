#ÖGELERE ERİŞİM
'''liste[a:b]
 a dahil
 b dahil değil
 '''

def ornek1():
    thislist = ["apple", "banana", "cherry"]
    print(thislist[-1])

def ornek2():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
    print(thislist[:4])
#baştan 4. indekse kadar alır.

def ornek3():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:])
#ikinci indeksten başla sonuna kadar devam et


def ornek4():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])
'''-1 → mango
-2 → melon
-3 → kiwi
-4 → orange
-5 → cherry
'''
#-4. indexten başla (orange) -1. indexe kadar git AMA -1 dahil değil




#extend(): Başka bir listedeki öğeleri mevcut listeye eklemek için kullanılır.
def extend_ornegi():
    # extend()
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist)


#dongu listeleri
def dongu_ornegi():
    # for döngüsü
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)

#forListedeki tüm öğeleri yazdıracak kısa bir kod parçası:
def kısa_yol_ornegi():
    # list comprehension ile print
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]

#newlist = [expression for item in iterable if condition == True]. Bu koşul , yalnızca doğru olarak değerlendirilen öğeleri kabul eden bir filtre gibidir True.
def kısa_yol_ornegi2():
    '''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

'''
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist)


kısa_yol_ornegi2()


#NOTLAR
'''
LIST METHODS (Kısa Not)

append()  → sona eleman ekler
clear()   → listeyi temizler
copy()    → kopya oluşturur
count()   → eleman sayısını verir
extend()  → başka liste ekler
index()   → elemanın indexini verir
insert()  → belirli konuma ekler
pop()     → indexe göre siler
remove()  → değere göre siler
reverse() → ters çevirir
sort()    → sıralar
'''