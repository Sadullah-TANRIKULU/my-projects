print("""*****************************
\tHarf Notu Hesaplama Aracı
*****************************
""")

a=float(input("Vize1:"))
b=float(input("Vize2:"))
c=float(input("Final:"))

d=a*30/100+b*30/100+c*40/100

print("Toplam Not:{}".format(a*30/100+b*30/100+c*40/100))

if (d >=90):
    print("AA")
elif(90> d >=85):
    print("BA")
elif(85> d >=80):
    print("BB")
elif(80> d >=75):
    print("CB")
elif(75> d >=70):
    print("CC")
elif(70> d >=65):
    print("DC")
elif(65> d >=60):
    print("DD")
elif(60> d >=55):
    print("FD")
else:
    print("FF")










