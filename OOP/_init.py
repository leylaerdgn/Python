# 1. __init__ kullanımı (temel örnek)
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Emil", 36)

print(p1.name)
print(p1.age)

# 2. __init__ olmadan kullanım
class Person2:
    pass

p2 = Person2()
p2.name = "Tobias"
p2.age = 25

print(p2.name)
print(p2.age)

# 3. __init__ ile daha kolay kullanım
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p3 = Person3("Linus", 28)

print(p3.name)
print(p3.age)


# 4. Varsayılan değer kullanımı
class Person4:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p4 = Person4("Emil")
p5 = Person4("Tobias", 25)

print(p4.name, p4.age)
print(p5.name, p5.age)


# 5. Çoklu parametre kullanımı
class Person5:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p6 = Person5("Linus", 30, "Oslo", "Norway")

print(p6.name)
print(p6.age)
print(p6.city)
print(p6.country)