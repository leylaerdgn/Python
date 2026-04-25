import: Tüm modülü içe aktarır.
from...import...: Modülün içinden sadece istediğini alırsın.

--------------------------------------------
RE MODÜL İÇİN NOTLAR

Karakter	Anlam
.	        herhangi bir karakter
^	        başlangıç
$	        bitiş
*	        0 veya daha fazla
+	        1 veya daha fazla
?	        0 veya 1
{}	        belirli sayıda
[]	        karakter grubu
`	`


| Pattern | Anlam          |
| ------- | -------------- |
| `\d`    | sayı           |
| `\D`    | sayı olmayan   |
| `\s`    | boşluk         |
| `\S`    | boşluk olmayan |
| `\w`    | harf + sayı    |
| `\W`    | bunların dışı  |


--------------------------------------------

REQUST MODULE

| Method | Ne yapar    |
| ------ | ----------- |
| GET    | veri çek    |
| POST   | veri gönder |
| PUT    | güncelle    |
| DELETE | sil         |



| Kod | Anlam           |
| --- | --------------- |
| 200 | ✅ Başarılı      |
| 404 | ❌ Sayfa yok     |
| 500 | ❌ Sunucu hatası |


---------------------------------------------

HTTP: Açılımı Hyper Text Transfer Protokol olan HTTP, sunucular ile kullanıcıların birbirlerinden ayrıları ile nasıl haberleşeceğini anlatan bir protokoldür(kurallar). Biz google'a girip bir şey arattığımız zaman sunuculara bir istek atarız ve bunun sunucunda sunucu bize bir yanıt gönderir. İşte bu iletişim sırasında uyulması gereken kurallara HTTP denir.

HTTP Metotları
-GET
-POST
-DELETE
-HEAD
-PUT
-PATCH
-OPTIONS