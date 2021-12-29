print("Yakıt Maliyeti Hesap Aracı")

a = float(input("kilometre başına yakıt(lt):"))
b = float(input("katettiği mesafe (km):"))
c = float(input("yakıt tutarı (lt):"))

print("ödenecek tutar hesaplanıyor...")

print("Toplam ödeme:\t{} TL'dir.".format(a*c*b))
