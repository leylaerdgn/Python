try:
    dosya=open("data.txt","r")
    icerik=dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya Bulunamadı.")
finally:
    dosya.close()
    print("Dosya Kapatıldı.")