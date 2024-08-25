import random

x=int(input('num:'))
y=int(input('num1 :'))


while True:
    try:

        s=int(random.randint(0,10))
        p=int(random.randint(0,10))

        a=s+p
        b=s*p
        a==x and b==y
        if a == x and b==y :
            print(s,p)
            break
        else:
            continue
    except:
        print('sorry')






