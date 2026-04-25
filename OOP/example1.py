class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        total = 0
        for p in self.products:
            total += p.price
        return total


p1 = Product("Laptop", 20000)
p2 = Product("Mouse", 500)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

print("Toplam:", cart.total_price())