#Python’da internet üzerinden veri çekmek ve göndermek için kullanılır
#Yani API’lerle konuşmanı sağlar
#Yerleşik değildir, kurman gerekir: pip install requests

import requests

# 1. GET isteği (veri çekme)
url_get = "https://jsonplaceholder.typicode.com/users"
response_get = requests.get(url_get)

status_code = response_get.status_code #Bu, isteğin başarılı olup olmadığını söyler
text_data = response_get.text

# JSON'a çevirme
json_data = response_get.json()
ilk_kullanici_adi = json_data[0]["name"] if json_data else None


# 2. POST isteği (veri gönderme)
url_post = "https://jsonplaceholder.typicode.com/posts"
gonderilecek_veri = {
    "title": "Test",
    "body": "Hello",
    "userId": 1
}
response_post = requests.post(url_post, json=gonderilecek_veri)
post_sonuc = response_post.json()


# 3. Sonuçları değişkenlerde tutma (gerekirse kullanırsın)
sonuclar = {
    "status_code": status_code,
    "ilk_kullanici": ilk_kullanici_adi,
    "post_cevap": post_sonuc
}

# örnek kullanım (isteğe bağlı)
print(sonuclar)