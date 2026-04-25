#JSON = veri saklama ve veri gönderme formatı
#Metin tabanlıdır (string gibi)
#Genelde API’lerde kullanılır
#JSON = veri taşıma formatı
#Python = işlem yapma

import json

#json.loads(): JSON stringi Python nesnesine çevirir.
json_veri = '{ "name":"John", "age":30, "city":"New York"}'
python_veri = json.loads(json_veri)
yas = python_veri["age"]  # 30. JSON -> dict olur.

#dumps(): Python nesnesini JSON stringine çevirir.
python_obj = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(python_obj) #dict -> JSON string





