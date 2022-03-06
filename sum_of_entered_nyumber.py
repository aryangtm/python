x=int(input())
sum=0
for i in range(1,x+1,1):
    r=x%10
    sum=sum+r
    x=x//10
print(sum)
