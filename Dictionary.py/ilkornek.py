ogrenciler= {}
number = input("Öğrenci no: ")
name= input("Öğrenci adı: ")
surname= input("Öğrenci soyadı: ")
phone= input("Öğrenci telefonu: ")

ogrenciler[number] ={
'ad': name,
'soyad': surname,
'telefon': phone,
}
print(ogrenciler)