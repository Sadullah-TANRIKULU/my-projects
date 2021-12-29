print("\tGeometrik Şekil Hesaplama Aracı:")

Geoşekil=input("Dörtgen mi? Üçgen mi? Yazınız.:")

if Geoşekil=="Dörtgen":
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))
    d=float(input("d:"))
    if a==b and a==c and a==d:
        print("Kare")
    elif a==c and b==d:
        print("Dikdörtgen")
    else:
        print("Yamuk")
elif Geoşekil=="Üçgen":
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))
    if abs(a + b) > c and abs(c + b) > a and abs(a + c) > b:
        if a==b and a==c:
            print("Eşkenar Üçgen")
        elif ((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen Belirtmiyor")
else:
    print("Geçersiz şekil...")
















