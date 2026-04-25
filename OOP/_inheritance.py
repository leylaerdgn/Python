# 1. Üst sınıf oluşturma
print("---- Örnek 1: Üst sınıf ----")
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


# 2. Alt sınıf (hiçbir şey eklemeden)
print("\n---- Örnek 2: Basit kalıtım ----")
class Student1(Person):
    pass

x = Student1("Mike", "Olsen")
x.printname()


# 3. __init__ ekleme (manuel)
print("\n---- Örnek 3: __init__ + Person.__init__ ----")
class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student2("Ali", "Veli")
x.printname()


# 4. super() kullanımı
print("\n---- Örnek 4: super() ----")
class Student3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student3("Ayşe", "Kaya")
x.printname()


# 5. Yeni özellik ekleme
print("\n---- Örnek 5: Yeni özellik ----")
class Student4(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student4("Mehmet", "Demir", 2024)
print(x.firstname, x.lastname, x.graduationyear)


# 6. Yeni metot ekleme
print("\n---- Örnek 6: Yeni metot ----")

class Student5(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)

x = Student5("Zeynep", "Yılmaz", 2025)
x.welcome()


# 7. Override (metodu ezme)
print("\n---- Örnek 7: Override ----")

class Student6(Person):
    def printname(self):
        print("Student:", self.firstname, self.lastname)

x = Student6("Can", "Koç")
x.printname()  # üst sınıf değil, bu çalışır