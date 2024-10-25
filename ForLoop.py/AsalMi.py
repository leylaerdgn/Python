sayi=int(input("Sayı Giriniz: "))
asalMi=True

if sayi==1:
    asalMi=False
else: 
    for i in range(2,sayi):
        if(sayi%i==0):
            asalMi=False
            break
if asalMi:
      print(f'{sayi} asaldır.')

else:
     print(f'{sayi} asal değildir')







