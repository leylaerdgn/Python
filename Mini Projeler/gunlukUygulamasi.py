from datetime import datetime

while True:
   secim=int(input("Seçiminz:\n1) Not Ekle\n2) Notları Oku\n3) Çıkış\n"))
   
   if secim==1:
      yazma=input('Ne yazmak istersiniz: ')
      tarih= datetime.now().strftime("%Y-%m-%d %H:%M")

      with open("ornek.txt", "a", encoding="utf-8") as file:
         file.write(f"[{tarih}] {yazma}\n")

   elif secim==2:
      try:
        with open("ornek.txt","r", encoding="utf-8") as file:
           print(file.read())
      except FileNotFoundError:
        print("dosya bulunamadı!") 
      
   elif secim==3:
      break
   
   else:
      print("Geçersiz seçim.")
