#Sözlükler, veri değerlerini anahtar:değer çiftleri halinde saklamak için kullanılır.
#Sözlük, sıralı*, değiştirilebilir ve yinelenen öğelere izin vermeyen bir koleksiyondur.

def ornek():
    thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
               }
    print(thisdict)


#Sözlüğün marka değerini yazdır:
def ornek1():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict["brand"])


#yinelenen kayıtlara izin vermez:
def ornek2():
    thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
    }
    print(thisdict)

#dict() ile sözlük oluşturmak mümkün:
def ornek3():
    thisdict = dict(name = "John", age = 36, country = "Norway")
    print(thisdict)


#ÖGELERE ERİŞİM

#GET(): değer alır.
def ornek4():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
    }
    x = thisdict.get("model")
    print(x)

#keys(): anahtarları alır.
def ornek5():
    thisdict = dict(name = "John", age = 36, country = "Norway")
    x = thisdict.keys()
    print(x)

#values(): değerleri alır.
def ornek6():
    thisdict = dict(name = "John", age = 36, country = "Norway")
    x = thisdict.values()
    print(x)


#items(): Sözlükteki tüm anahtar-değer (key-value) çiftlerini birlikte verir.
def ornek7():
    thisdict = dict(name = "John", age = 36, country = "Norway")
    x = thisdict.items()
    print(x)

'''
-Yılı" 2018 olarak değiştirin:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

-----------------------------

- Sözlüğü güncelleyin:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

-----------------------------

-Öge ekleyin:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

-----------------------------

-Öge kaldırın:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

-----------------------------

-Sözlükteki tüm anahtar isimleri tek tek yazdır:
for x in thisdict:
  print(x)

  -----------------------------

-Sözlükteki tüm değerleri tek tek yazdırın:
for x in thisdict:
  print(thisdict[x])

-----------------------------

-values(): Bu yöntemi bir sözlüğün değerlerini döndürmek için de kullanabilirsiniz :
for x in thisdict.values():
  print(x)


'''