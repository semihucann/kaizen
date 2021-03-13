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
#### Example Outputs
```bash
bash@bash  ~/Desktop/kaizen  python3 code.py             
Num	  Code
0.	  7C2D4947
1.	  3E72E277
2.	  E542A23D
3.	  C3737443
4.	  D323A5F4
5.	  9D4CD25D
6.	  79A23DEA
7.	  C3A5EA9D
8.	  4FED745A
9.	  259279A3
10.	  5DEF3DC2
```

```bash
bash@bash  ~/Desktop/kaizen  python3 code.py -c 7C2D4947
True
```
```bash
bash@bash  ~/Desktop/kaizen  python3 code.py -c 7C2D4948
False
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

#### Example Outputs
```bash
bash@bash  ~/Desktop/kaizen  python3 parser.py          

TEŞEKKÜRLER 
GUNEYDOĞU TEKS. GIDA INS SAN. LTD.STI. 
ORNEKTEPE 
MAH.ETIBANK CAD.SARAY APT. 
N:43-1 BEYOĞLU/ISTANBUL 
GÜNEŞLİ V.D. 4350078928 V. NO. 
TARIH : 26.08.2020 
SAAT : 15:27 
FİŞ NO : 0082 
54491250 
2 ADx 2,75 
CC.COCA COLA CAM 200 08 
2701084 *5,50 
1,566 KGx 1,99 
MANAV DOMATES PETEME *3,32 
2701076 
0,358 KGx 4,99 
MANAV BIBER CARLISTO 08 *1,79 
4 
EKMEK CIFTLI 01 *1,25 
TOPKDV *0,80 
TOPLAM *11,86 
NAKİT *20,00 
KDV KDV TUTARI KDV'LI TOPLAM 
01 *0,01 *1,25 
08 *0,79 *10,61 
KASİYER : SUPERVISOR 
00 0001/020/000084/1//82/ 
PARA USTÜ *8,14 
KASİYER: 1 
2 NO:1330 EKÜ NO:0001 
MF YAB 15017876 
```
