#Parametre , fonksiyon tanımında parantez içinde listelenen değişkendir.
#Argüman , bir fonksiyon çağrıldığında ona gönderilen gerçek değerdir.
#*args: Fonksiyona istediğin kadar (sınırsız) parametre göndermeni sağlar

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
#my_function("Hello", "Emil", "Tobias", "Linus")

def my_function1(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
#print(my_function1(1, 2, 3))
#print(my_function1(10, 20, 30, 40))
#print(my_function1(5))


def my_function2(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
#print(my_function2(3, 7, 2, 9, 1))


#**kwargs: Fonksiyona anahtar-değer (key=value) şeklinde sınırsız veri gönderirsin
def my_function3(**kid):
  print("His last name is " + kid["lname"])
#my_function3(fname = "Tobias", lname = "Refsnes")