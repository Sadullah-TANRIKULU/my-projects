print("""
*****************************
Faktöriyel Bulma Programı

Çıkmak için 'q'ya basın.
*****************************""")

while True:
    sayı=input("Sayı:")
    if(sayı=="q"):
        print("Program sonlandırılıyor.")
        break

    else:
        sayı=int(sayı)

        faktoriyel = 1
        for i in range(2,sayı+1): # mesela 5'in faktöriyelini istediğimizde range kodu ile +1 yazmamız gerekiyor.
            print("Faktöriyel",faktoriyel,"i",i)
            faktoriyel *= i
        print("Faktöriyel",faktoriyel)
