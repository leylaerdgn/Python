# 1. self ile özelliklere erişim
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person1("Emil", 25)
p1.greet()


# 2. self sayesinde farklı nesneler
class Person2:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

p2 = Person2("Tobias")
p3 = Person2("Linus")

p2.printname()
p3.printname()


# 3. self yerine farklı isim kullanımı
class Person3:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc): #python ilk parametre neyse onu self gibi kullanır.
        print("Hello, my name is " + abc.name)

p4 = Person3("Emil", 36)
p4.greet()


# 4. Çoklu özellik kullanımı
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()


# 5. self ile metot çağırma
class Person5:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p5 = Person5("Tobias")
p5.welcome()