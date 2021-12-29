print("""*********************************
print("Hesap Makinesi Programı")

İşlemler:

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi

5. Üssü İşlemi

6. Kök İşlemi

7. Yüzde İşlemi
*********************************
""")

a=int(input("Birinci Sayı:"))
b=float(input("İkinci Sayı:"))

işlem= input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} in toplamı {} dir.".format(a,b,(a+b)))
elif işlem == "2":
    print("{} ile {} in farkı {} dir.".format(a,b,(a-b)))
elif işlem == "3":
    print("{} ile {} in çarpımı {} dir.".format(a,b,(a*b)))
elif işlem == "4":
    print("{} ile {} in bölümü {} dir.".format(a,b,(a/b)))
elif işlem == "5":
    print("{} in {} üssü {} dir.".format(a,b,(a**b)))
elif işlem == "6":
    print("{} in {} kökü {} dir.".format(a,b,(a**b)))
elif işlem == "7":
    print("{} in yüzde{} si {} dir.".format(a,b,(a*b/100)))

else:
    print("Geçersiz işlem.......")