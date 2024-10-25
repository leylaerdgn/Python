try:
 file=open("newfile2.txt","r",encoding='utf-8')
except FileNotFoundError:
 print("dosya okuma hatası")
finally:
 print("dosya kapandı.")
 file.close()