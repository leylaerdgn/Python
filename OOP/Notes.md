Class içinde değişkenler ve metotlar tanımlanır.

Bir sınıf, bir nesnenin nasıl görünmesi gerektiğini tanımlar ve bir nesne bu sınıfa göre oluşturulur. Bir sınıftan bir nesne oluşturduğunuzda, o nesne o sınıf içinde tanımlanmış tüm değişkenleri ve fonksiyonları miras alır.

------------------------------------------

__init__ içinde self ile tanımladığın şeylere,
diğer metotlarda self yazarak erişebilirsin

__init__() → sınıftan nesne oluşturulunca otomatik çalışan metot
Amaç: Nesneye başlangıç değerleri vermek, Gerekli ayarları yapmak
self ile yazılan değişkenler: Nesneye ait olur (her metotta kullanılabilir)
Neden kullanılır?
 __init__ olmazsa: Her nesne için değerleri tek tek manuel vermen gerekir
 __init__ ile: Nesne oluştururken direkt değer verirsin

-------------------------------------------

self → oluşturulan nesnenin kendisini temsil eder
Amaç: Nesnenin özelliklerine (name, age vs.) erişmek
Nesnenin diğer metotlarını çağırmak

Özellikler:
-self, her instance metodun ilk parametresi olmalı
-self.name gibi kullanılır → nesneye ait veri
-Her nesne için self farklıdır

Çünkü Python şunu bilmek zorunda: Hangi nesnenin verisini kullanacağım?

Neler yapabiliriz?
Özelliklere erişim → self.name
Metot çağırma → self.greet()

------------------------------------------

Sınıf özellikleri (attributes) nedir?
Sınıfa ait değişkenlerdir. Nesnelerin veri tutmasını sağlar
-Türleri
1. Instance (nesne) özelliği
self.name = name
✔️Her nesneye özeldir
✔️__init__ içinde tanımlanır

2. Class (sınıf) özelliği
species = "Human"
✔️ Tüm nesneler ortak kullanır

🔸 Neler yapabiliriz?
✔️ Özelliklere erişim
→ p1.name
✔️ Değiştirme
→ p1.age = 26
✔️ Silme
→ del p1.age
✔️ Yeni özellik ekleme
→ p1.city = "Oslo"

-------------------------------------------

Sınıf metotları nedir?
Sınıf içinde tanımlanan fonksiyonlardır
Nesnelerin davranışlarını belirler
Temel kurallar
✔️ Her metodun ilk parametresi → self
✔️ Nesne üzerinden çağrılır → p1.greet()

Neler yapabilir?
1. Parametre alabilir: calc.add(5, 3)
2. Nesne özelliklerine erişir: self.name
3. Özellikleri değiştirebilir: self.age += 1
4. Özel metotlar (magic methods)
 __str__()
print(obj) çalışınca ne yazılacağını belirler
5. Birden fazla metot olabilir. Aynı sınıfta birçok metot birlikte çalışabilir
6. Metot silme: del Person.greet

--------------------------------------------

Kalıtım (Inheritance) nedir?
 Bir sınıfın, başka bir sınıfın özelliklerini ve metotlarını almasıdır

🔸 Terimler
Üst sınıf (Parent / Base) → miras veren
Alt sınıf (Child / Derived) → miras alan
🔸 Nasıl yapılır?
class Student(Person): Student, Person’dan her şeyi alır

🔸 pass: “Şimdilik bir şey eklemiyorum” demek

🔸 __init__ konusu
Alt sınıfta __init__ yazarsan üst sınıfın __init__'i çalışmaz

✔️ Bu yüzden çağırman gerekir:

Person.__init__(self, fname, lname)

veya daha doğru yol: super().__init__(fname, lname)

🔸 super(): Üst sınıfa erişir. Kod yazmayı kolaylaştırır

🔸 Alt sınıfa ekleme yapma

Yeni özellik ekleyebilirsin:

self.graduationyear = year

✔️ Yeni metot ekleyebilirsin:

def welcome(self):

🔸 Override (ezme): Alt sınıfta aynı isimde metot yazarsan üst sınıfın metodu geçersiz olur

---------------------------------------------

Polimorfizm: Aynı isimde fonksiyon/metot farklı şekillerde çalışır

1. Fonksiyon Polimorfizmi
Aynı fonksiyon farklı veri tiplerinde çalışır

Örnek:
len("abc") → karakter sayısı
len([1,2,3]) → eleman sayısı
len(dict) → key sayısı

2. Sınıf Polimorfizmi
Farklı sınıflar aynı isimde metot kullanır

move()
Ama:
Car → Drive
Boat → Sail
Plane → Fly

3. Kalıtım + Polimorfizm
Alt sınıflar: Üst sınıftan metot alır. İsterse override eder

-------------------------------------------

Kapsülleme (Encapsulation): Verileri korumak ve kontrol etmek

Verileri sınıf içinde tutarsın. Dışarıdan erişimi sınırlandırırsın
🔸 Türler
1. Private (Özel): Dışarıdan direkt erişilemez. Getter / Setter ile erişilir. __age

2. Protected (Koruma): Erişilebilir ama “kullanma” uyarısıdır (kural). _salary

🔸 Getter & Setter
✔️ Getter → veri okuma
✔️ Setter → veri değiştirme (kontrollü)


🔸 Private metot: Sadece class içinde kullanılır.class DIŞINDAN erişemezsin
Class İÇİNDEN erişebilirsin

🔸 Name Mangling (isim değiştirme):  Python arka planda ismi değiştirir
__age → _Person__age

----------------------------------------------

İç sınıf (Nested Class): Bir sınıfın içinde tanımlanan başka bir sınıf

🔸 Temel mantık
class Outer:
    class Inner:

-> Inner, Outer’ın içinde

🔸 Nasıl kullanılır?
✔️ Önce dış sınıf oluşturulur
✔️ Sonra iç sınıftan nesne oluşturulur

outer = Outer()
inner = outer.Inner()

🔸 Önemli nokta : İç sınıf dış sınıfa otomatik erişemez. Eğer erişmesi gerekiyorsa:

inner = outer.Inner(outer)
