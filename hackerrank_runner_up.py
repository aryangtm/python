n=int(input())
lst=[]
temp=0
lst.extend([int(i)for i in input().split()])
l=max(lst)
s=min(lst)
for i in range(0,n):
    if(lst[i]>s and lst[i]!=l):
        s=lst[i]
print(s)
    
