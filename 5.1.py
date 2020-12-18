y=int(input('введите значение y: '))
a=int(input('введите значение a: '))
p=int(input('введите значение p: '))

for x in range(0,p):
    if (a**x)%p==y:
        print("Ответ: x = ",x)
        print(y," = ",a,"^",x,"mod",p)
        break
