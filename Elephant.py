x = int(input())
if x==1 or x==2 or x==3 or x==4 or x==5:
    print(1)
else:
    a = x//5
    b = x%5
    if b == 0:
        print(a)
    else:
        print(a+1)
