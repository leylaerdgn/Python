#Girilen parola içinde turkce karakter hatası veriniz.
turkce_karakterler='şçöğüıİ'
parola=input("Parola: ")
for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola türkçe karakter içermez. ')
    else:
        pass 
    print('Geçerli parola')