# Kaizen Case Study

## Question 1 
GenerateCode:
1. Salt Key belirlendi.
2. Salt Key ile 1-1000 string değerleri birleştirildi.
3. Elde edilen 1000 adet salted data sha256 hash fonksiyonundan geçirildi.
4. Hashlenmiş verilerin herbirisinin istenen karakter kümesinden olan ilk 10 karakteri alındı ve kod üretildi.

#### To Run
* Generate all codes:
```bash
$ python3 code.py
```

* Check one code:
```bash
$ python3 code.py -c <CODE>
```

## Question 2 
1. Response.json data yükleniyor.
2. Her bir düğüme ait 4 köşe ayıklanıyor.
3. 4 Köşeyi temsil eden 8 nokta 4 noktaya indirgeniyor. (start_x-stop_x; start_y-stop_y)
4. Her cümleyi temsil eden x ve y aralıklarının ortalaması alınıyor.
5. Satır aralıkları yaklaşık olarak 20br olduğu için her cümle ortalama y değeri 20 ile integer bölmesine tabi tutuluyor ve hangi satırda olduğu tespit ediliyor.
6. Response.json yeni bir dizi içerisinde bu veriler ile temsil ediliyor. (Description, ortalama_x, ortalama_y)
7. OCR'dan dönen response sıralı gelmediği için y(satır numaralarına) göre sıralanıyor.
8. Son bölümde de aynı satırda olanlar boşluk, farklı satırda olanlar "\n" eklenerek stringde birleştiriliyor.


#### To Run
```bash
$ python3 parser.py
```


