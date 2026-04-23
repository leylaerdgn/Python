#Sayfa sonunda guncelleme
#with open("deneme.txt","a",encoding="utf-8") as file:
# file.write("\nLeyla Erdoğan")


#Sayfa başında guncelleme
with open("newfile.txt","r+") as file:
    content=file.read()
    content="Zeynep Erdoğan\n" +content
    file.seek(0)
    file.write(content)
with open("newfile.txt","r", encoding="utf-8"):
    print(file.read())
