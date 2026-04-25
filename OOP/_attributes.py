# 1. Temel özellik kullanımı
print("---- Örnek 1: Temel özellik ----")
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Emil", 36)

print(p1.name)
print(p1.age)


# 2. Özelliklere erişim
print("\n---- Örnek 2: Özelliklere erişim ----")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)


# 3. Özellik değiştirme
print("\n---- Örnek 3: Özellik değiştirme ----")
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person2("Tobias", 25)
print(p2.age)

p2.age = 26
print(p2.age)


# 4. Özellik silme
print("\n---- Örnek 4: Özellik silme ----")
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p3 = Person3("Linus", 30)

del p3.age

print(p3.name)
# print(p3.age)  # HATA verir


# 5. Class vs Instance özelliği
print("\n---- Örnek 5: Class vs Instance ----")
class Person4:
    species = "Human"  # Class property

    def __init__(self, name):
        self.name = name  # Instance property

p4 = Person4("Emil")
p5 = Person4("Tobias")

print(p4.name)
print(p5.name)
print(p4.species)
print(p5.species)


# 6. Class özelliği değiştirme
print("\n---- Örnek 6: Class özelliği değiştirme ----")
class Person5:
    lastname = ""

    def __init__(self, name):
        self.name = name

p6 = Person5("Linus")
p7 = Person5("Emil")

Person5.lastname = "Refsnes"

print(p6.lastname)
print(p7.lastname)


# 7. Yeni özellik ekleme
print("\n---- Örnek 7: Yeni özellik ekleme ----")
class Person6:
    def __init__(self, name):
        self.name = name

p8 = Person6("Tobias")

p8.age = 25
p8.city = "Oslo"

print(p8.name)
print(p8.age)
print(p8.city)