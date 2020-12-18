import numpy as np
import math
from math import sqrt
y=int(input('введите значение y: '))
a=int(input('введите значение a: '))
p=int(input('введите значение p: '))

for i in range(0,round(sqrt(p))+1):
    if i**2>p:
        k=i
        print("k = ",k)
        m=i
        print("m = ",m)
        break
    if i*(i+1)>p:
        k=i
        print("k = ",k)
        m=i+1
        print("m = ",m)
        break

x1=np.zeros(m)
print ("Шаг младенца")
for i in range(0,m):
    x1[i]=(y*(a**i))%p
print(x1)

x2=np.zeros(k)
print ("")
print ("Шаг великана")
for i in range(1,k+1):
    x2[i-1]=(a**(m*i))%p
print(x2)
for k1 in range(0,m):
    for k2 in range(0,k):
        if (x1[k1]==x2[k2]):
            i=k2+1
            j=k1
            print("(a^",i,"m)mod p = ((a^",j,")*y)mod p")
            break
x=i*m - j
print("Ответ: x = ",x)
print(y," = ",a,"^",x,"mod",p)

           
