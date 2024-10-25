class Circle:
    pi=3.14
    def __init__(self, yaricap=1):
        self.yaricap=yaricap

    def cevreHesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
    
c1=Circle()
c2=Circle(5)

print(f'c1: alan= {c1.alan_hesapla()} cevre= {c1.cevreHesapla()}')
print(f'c2: alan= {c2.alan_hesapla()} cevre= {c2.cevreHesapla()}')

    