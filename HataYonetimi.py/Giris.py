while True:
    sayi=input('Sayı: ')
    if sayi=='q':
        break

    try:
        result=float(sayi)
        print('Girdiğiniz sayı: ',result)
        
    except ValueError:
        print('Geçersiz sayı')
        continue