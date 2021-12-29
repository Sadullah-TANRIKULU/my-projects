print("\tBeden Kitle İndeksi Hesaplama Aracı:")

a = int(input("Kilo(kg):"))
b = float(input("Boy(m):"))

c = a/b**2
print("BKI:{}".format(c))
if c < 18.5:
    print("zayıf")
elif 25 > c >= 18.5:
    print("normal")
elif 30 > c >= 25:
    print("Fazla kilolu")
elif c >= 30:
    print("Obez")
