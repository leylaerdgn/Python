import os
result=dir(os)
result=os.name

#dizin degistirme
#os.chdir('c://')
#os.chdir('../..')

#etkin dizin öğrenme
#result=os.getcwd()

#klasör olusturma
#os.mkdir("newdirectory")
#os.makedirs("newdirectory/yeniklasor")

#listeleme
#result=os.listdir('c://')
#eger filtreleme yapmak istiyorsak
#for dosya in os.listdir():
#    if dosya.endswith('.py'):
#     print(dosya)

#bir dosya hakkında bilgi sahibi olmak istersek
#result=os.stat("ForLoop.py")

#klasör ismini degistirmek istersek
#os.rename("newdirectory","yeniklasor")
#silmek istersek
#os.rmdir("newdirectory")

#Dosyanın tam konumunu belirtmek için
#result=os.path.abspath("ilkders.py")

#Dizin ismini almak için
#result=os.path.dirname(os.path.abspath("ilkders.py"))

#Boyle bir dosya var mı?
#result=os.path.exists('ilkders.py')

#Klasor mu?
#result=os.path.isdir("C:/Users/LEYLA ERDOĞAN/Desktop/Python/ForLoop.py")

#Dosya mı?
result=os.path.isfile("C:/Users/LEYLA ERDOĞAN/Desktop/Python/ForLoop.py")
print(result)
