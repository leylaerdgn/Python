#Demetler (tuples), birden fazla öğeyi tek bir değişkende saklamak için kullanılır.
#Bir demet (tuple), sıralı ve değiştirilemez bir koleksiyondur .
#Yalnızca bir öğeden oluşan bir demet (tuple) oluşturmak için, 
##öğenin sonuna virgül eklemeniz gerekir; aksi takdirde Python bunu demet olarak tanımaz.
def tek_tuple():
   thistuple = ("apple",)
   print(type(thistuple))

#TUPLE DEĞERLERİNİ DEĞİŞTİR
'''
Bir demet (tuple) oluşturulduktan sonra, değerlerini değiştiremezsiniz. Demetler değiştirilemez veya diğer adıyla sabittir .
Ancak bir çözüm yolu var. Demeti bir listeye dönüştürebilir, listeyi değiştirebilir ve listeyi tekrar demete dönüştürebilirsiniz.
'''
def tuple_degistir():
   x = ("apple", "banana", "cherry")
   y = list(x)
   y[1] = "kiwi"
   x = tuple(y)
   print(x)