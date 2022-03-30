n=int(input())
lst=[]
sum=0
lst=list(map(eval,input().split()))
for i in range(0,n):
    sum=sum+lst[i]
print(sum)
