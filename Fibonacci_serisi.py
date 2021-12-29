"""
Fibonacci serisi 1,1 ile başlar. Yeni sayı önceki iki sayının toplamı ile oluşur.
"""
a=1
b=1
fibonacci=[a,b]

for i in  range(10):
    a,b=b,a+b
    print("a:",a,"b:",b)
    fibonacci.append(b)
print(fibonacci)