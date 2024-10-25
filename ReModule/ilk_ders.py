#Düzenli ifadelerle çalışmayı saglar
import re

str="Python Kursu: Python Programlama Rehberiniz | 40 saat"
#result=re.findall("Python", str)

#result=re.split(" ",str)
#result=re.split("R",str)

#result=re.sub(" ", "-",str)

#result=re.search("Python",str)

#result=re.findall("[abc]",str)

#result=re.findall("[^0-9]",str)

#result=re.findall("Py..on",str)

#result=re.findall("^P",str)

result=re.findall("t$",str)
print(result)