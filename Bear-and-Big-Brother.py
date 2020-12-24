l, b = map(int, input().split())
years = 0
while l<b or l==b:
    l = l*3
    b = b*2
    years = years+1
print(years)
