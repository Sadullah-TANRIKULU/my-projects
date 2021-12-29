sayi = int(input("Bir sayı giriniz:"))

basamak = str(sayi)
toplam = 0
for i in basamak:
    rakam = (int(i)**len(basamak))
    toplam += rakam
if sayi == toplam:
    print(sayi, "bir armstrong sayısıdır.")
else:
    print(sayi, "bir armstrong sayısı değildir.")
