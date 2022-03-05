sum=0
m=int(input())
while m>0:
    r=m%10
    sum=sum*10+r
    m=m//10
print(sum)
