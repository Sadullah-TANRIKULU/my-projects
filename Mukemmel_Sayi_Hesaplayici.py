sayı=int(input("Bir sayı giriniz:"))

i=1
toplam=0

while(i<sayı):
    if(sayı % i == 0):
        toplam +=i
    i += 1
if(sayı == toplam):
    print(sayı,"mükemmel bir sayıdır.")
else:
    print(sayı,"mükemmel sayı değildir.")