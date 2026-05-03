liste=[]
while True: 
     print("İşleminizi seçiniz:\n1- Ekle\n2- Sil\n3- Listele\n4- Çıkış")
     secim=input('Seçiminiz: ')

     if secim=="1":
          urun=input("Eklenecek ürün gir: ")
          liste.append(urun)
     elif secim=="2":
          urun=input("Çıkarılacak ürünü seç: ")
          if urun in liste:
                liste.remove(urun)
          else:
               print('Ürün listede yok')
     elif secim=="3":
          print("'Liste: ",liste)
     elif secim=="4": 
          print("Çıkış yaptınız!")
          break
     else:
          print('Geçersiz işlem!')
          