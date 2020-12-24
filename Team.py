n = int(input())
a = []
for i in range(n):
    p, v, t = map(int, input().split())
    b = [p,v,t]
    a.append(b)
d = 0
for j in a:
    c = j.count(1)
    if c>1:
        d+=1
print(d)
