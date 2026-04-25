# 1. Private property
print("---- Örnek 1: Private property ----")
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private

p1 = Person1("Emil", 25)
print(p1.name) # print(p1.__age)  # HATA verir


# 2. Getter kullanımı
print("\n---- Örnek 2: Getter ----")
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p2 = Person2("Tobias", 25)
print(p2.get_age())


# 3. Setter kullanımı
print("\n---- Örnek 3: Setter ----")
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p3 = Person3("Tobias", 25)
print(p3.get_age())

p3.set_age(26)
print(p3.get_age())


# 4. Kapsülleme örneği (doğrulama)
print("\n---- Örnek 4: Kapsülleme ----")
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())


# 5. Protected property
print("\n---- Örnek 5: Protected ----")
class Person4:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # protected

p4 = Person4("Linus", 50000)
print(p4.name)
print(p4._salary)  # erişilir ama önerilmez


# 6. Private method
print("\n---- Örnek 6: Private method ----")
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5)  # HATA


# 7. Name mangling
print("\n---- Örnek 7: Name mangling ----")
class Person5:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p5 = Person5("Emil", 30)

print(p5._Person5__age)  # teknik olarak erişilebilir (önerilmez)