def Arttir(x):
    return x*1.2
personel=["Ali","Veli","Can","Canan","Kemal"]
maas=[1000,2000,2500,3000,3500]
yeniMaas=list(map(Arttir,maas))
sonuc=list(zip(personel,yeniMaas))
for i,k in sonuc:
    print("{} isimli personelin zamlı maaşı: {}".format(i,k))