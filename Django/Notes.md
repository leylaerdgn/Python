Normalde bir web sitesi yaparken:
-URL yönetimi
-Kullanıcıdan veri alma
-Veritabanı işlemleri
-Güvenlik
-Oturum (login/logout)
gibi şeyleri tek tek sen yazmak zorunda kalırsın. Ama bir web framework kullanırsan: Bunların çoğu hazır gelir.

DJANGO
- >Django, Python programlama dili ile yazılmış yüksek seviyeli bir web framework’üdür.
->Web siteleri ve web uygulamaları geliştirmeyi hızlı ve kolay hale getirir.
->“Don’t Repeat Yourself (DRY)” yani tekrardan kaçın prensibini benimser.
->İçinde birçok hazır özellik gelir, böylece sıfırdan her şeyi yazmak zorunda kalmazsın.

- >Öne çıkan özellikleri
-Hazır admin paneli (veri yönetimi için)
-ORM sistemi (veritabanı işlemlerini kolaylaştırır)
-Güvenlik (CSRF, XSS gibi saldırılara karşı koruma)
-URL routing sistemi
-Template sistemi (HTML oluşturma)

- >En önemli mantık: MVT yapısı
Model (Veri): Veritabanı ile ilgilenir. Veriler burada tutulur. Örneğin film adı, kullanıcı bilgisi.

View: İstekleri karşılar. Ne yapılacağına karar verir. Örnek: Ana sayfa açıldı → hangi veriler gösterilecek?

Template: Kullanıcıya görünen kısım


- >Tüm süreç 
Bir kullanıcı siteye girince:

1. Tarayıcı → URL gönderir

2. Django → urls.py kontrol eder

3. Doğru → view çağrılır

4. View → modelden veri çeker

5. View → template’e veri gönderir

6. Template → HTML oluşturur

7. Tarayıcı → sonucu gösterir

- >django-admin startproject proje_adi
bu komut: yeni bir Django projesi oluşturur.

📁 Otomatik olarak:
proje_adi/
    manage.py
    proje_adi/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

1) manage.py: Projeyi kontrol ettiğin ana komut dosyası.
2) __init__.py: Pythona burası bir paket der. Genelde içi boş olur.
3) settings.py: Projenin beynidir. Her şey buradan ayarlanır ( VT, yüklü app'ler, güvenlik ayarları, dil/saat, static dosyalar vs)
4) urls.py: Siteye gelen URL'leri yöneten dosyadır.
5) wsgi.py: Projeyi web servera bağlayan dosyadır.
6) asgi.py: web sunucusu (Uvicorn, Daphne gibi) ile web çerçevesi (Django, FastAPI gibi) arasında iletişimi sağlayan, asenkron (eşzamansız) bir standart dosya ve protokoldür


- >python manage.py startapp movies
Projede ‘account’ ve 'moveies' adında yeni bir uygulama (app) oluştur.
home/
    __init__.py
    admin.py
    apps.py
    models.py
    views.py
    tests.py
    migrations/

1) views.py: Kullanıcı siteye girince ne görsün onu yazarsın
2) models.py: Verilerin yapısını tanımlarsın
3) admin.py: Modelleri admin panelinde görünür yaparsın. Veri ekleme/silme işlemleri buradan yapılır
4) apps.py: App ayarları (genelde dokunmazsın)
5) tests.py: Test yazmak için
6) migrations/: Models’ta yaptığın değişiklikleri kaydeder. Django veritabanını buna göre günceller

Oluşturduğumuz uygulamaları movieapp'e tanıtmamız gerekiyor. Bunun için movieapp ->settings.py dosyasına gidilir. orada installed_apps mevcut burada projeyi oluşturan uygulamalar tanımlanır.

--------------------
- >view.py
render: HTML dosyasını al -> kullanıcıya göster


---------------------
- >movies/urls.py
* from . import views:  Aynı klasördeki views.py dosyasını al. buradaki nokta aynı dizin demek.

* urlpatterns: Bu djangonun URL listesi demek. Amacı: Hangi URL -> hangi fonksiyona gidecek.
 path("", views.home),

| URL       | Gittiği yer |
| --------- | ----------- |
| `/`       | `home`      |
| `/about/` | `about`     |

http://127.0.0.1:8000/ → home fonksiyonuna gider

-------------------------
- >movieapp/urls.py (ANA URL)

* include:  Başka bir urls.py dosyasını içeri dahil etmek. Neden include kullanıyoruz:
Büyük projede her şeyi tek dosyaya yazmak karmaşıktır. Bunun yerine
Ana proje → yönlendirme yapar
App’ler → kendi URL’lerini yönetir

-------------------------
- > index.html
* {% ... %} (İşlem Etiketleri): Bu işaretler arasında bir "iş" yapılır. Döngü kurmak (for), bir şartı kontrol etmek (if) gibi mantıksal işlemler burada gerçekleşir. Ekranda doğrudan bir çıktı vermezler, sadece arka planda süreci yönetirler.

* {{ ... }} (Yazdırma Etiketleri): Bu işaretler ise "Bunu ekrana yaz!" demektir. Değişkenin içindeki veriyi (film adını, süresini vb.) kullanıcıya gösterir.

* {% load static %}: Django’ya şunu söylersin: Static (CSS, JS, resim) dosyalarını kullanacağım
Kullanım: {% load static %}
<img src="{% static 'images/logo.png' %}" alt="">
{% load static %} → sistemi açar
{% static '...' %} → doğru yolu bulur