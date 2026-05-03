def kmmil(km):
    return km * 0.621

def milkm(mil):
    return mil / 0.621

def cf(c):
    return (c * 9/5) + 32

def fc(f):
    return (f - 32) * 5/9

while True:
    secim = input("1- Km-Mil\n2- Mil-Km\n3- C-F\n4- F-C\n5- Çıkış\nSeçim: ")

    if secim == "1":
        km = float(input("Km: "))
        print(kmmil(km))

    elif secim == "2":
        mil = float(input("Mil: "))
        print(milkm(mil))

    elif secim == "3":
        c = float(input("C: "))
        print(cf(c))

    elif secim == "4":
        f = float(input("F: "))
        print(fc(f))

    elif secim == "5":
        break
     
    else:
      print("Geçersiz seçim!")
