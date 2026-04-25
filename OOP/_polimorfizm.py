# 1. Fonksiyon Polimorfizmi
print("---- Örnek 1: len() ----")
x = "Hello World!"
print(len(x))

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))


# 2. Sınıf Polimorfizmi
print("\n---- Örnek 2: Sınıf polimorfizmi ----")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()


# 3. Kalıtım + Polimorfizm
print("\n---- Örnek 3: Kalıtım + polimorfizm ----")
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car2(Vehicle):
    pass

class Boat2(Vehicle):
    def move(self):
        print("Sail!")

class Plane2(Vehicle):
    def move(self):
        print("Fly!")

car2 = Car2("Ford", "Mustang")
boat2 = Boat2("Ibiza", "Touring 20")
plane2 = Plane2("Boeing", "747")

for x in (car2, boat2, plane2):
    print(x.brand)
    print(x.model)
    x.move()