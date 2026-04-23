#Lambda, tek bir ifadeden oluşan küçük, isimsiz fonksiyonlardır. 
#Normal def ile tanımlanan fonksiyonlardan farklı olarak tek satırda yazılır ve hemen kullanılır.
#Söz Dizimi -> lambda argümanlar: ifade
def ornek1():
    x = lambda a: a + 10
    print(x(5))


def ornek2():
    x = lambda a, b: a * b
    print(x(5, 6))


def ornek3():
    def myfunc(n):
        return lambda a: a * n

    mydoubler = myfunc(2)
    print(mydoubler(11))

#Yaygın Kullanımları:

#MAP(): Her elemana aynı işlemi uygular ve yeni bir iterable döndürür.
def map_ornegi():
    # MAP()
    sayilar = [1, 2, 3, 4, 5]
    kareler = list(map(lambda x: x ** 2, sayilar))
    print(kareler)  # [1, 4, 9, 16, 25]

#FİLTER():Şarta uyan elemanları seçer (filtreler).
def filter_ornegi():
    # FILTER()
    sayilar = [1, 2, 3, 4, 5, 6]
    ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
    print(ciftler) # [2, 4, 6]

#SORTED(): Listeyi sıralar (orijinali değiştirmez, yeni liste döndürür).
def sorted_ornegi():
    # SORTED()
    students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
    sorted_students = sorted(students, key=lambda x: x[1])
    print(sorted_students)


