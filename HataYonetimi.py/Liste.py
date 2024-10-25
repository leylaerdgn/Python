#Liste elemanları içindeki sayısal değerleri bulunuz.
liste=["1","2","5a","10b","abc","50"]
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue