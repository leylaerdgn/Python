import requests
import json

api_key = "9165ca7a0ae1d24797bb037c"
api_url= f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü: " ) #USD
alinan_doviz = input ("Alınan döviz türü: ") #TRY
miktar = input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ") 

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json=json.loads(sonuc.text)
print(sonuc_json["conversion_rates"][alinan_doviz])