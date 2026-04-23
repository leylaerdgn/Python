#Dekoratör, bir fonksiyonun veya sınıfın davranışını değiştirmeden üzerine yeni özellikler ekleyen bir yapıdır. 
#Aslında bir fonksiyon alıp yine bir fonksiyon döndüren fonksiyondur
#@decorator_name olarak gösterilir.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())