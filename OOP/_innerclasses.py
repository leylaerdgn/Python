# 1. Basit iç sınıf
print("---- Örnek 1: Basit iç sınıf ----")
class Outer1:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

outer1 = Outer1()
print(outer1.name)


# 2. İç sınıfa erişim
print("\n---- Örnek 2: İç sınıfa erişim ----")

class Outer2:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class")

outer2 = Outer2()
inner2 = outer2.Inner()
inner2.display()


# 3. İç sınıftan dış sınıfa erişim
print("\n---- Örnek 3: Dış sınıfa erişim ----")

class Outer3:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f"Outer class name: {self.outer.name}")

outer3 = Outer3()
inner3 = outer3.Inner(outer3)
inner3.display()


# 4. Gerçek kullanım (Car - Engine)
print("\n---- Örnek 4: Car & Engine ----")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()


# 5. Çoklu iç sınıf
print("\n---- Örnek 5: Çoklu iç sınıf ----")

class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data...")

    class RAM:
        def store(self):
            print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()