n=int(input())
lst=[]
lst1=[]
lst=list(map(eval,input().split()))
lst1=list(map(eval,input().split()))
for i in range(0,n):
    lst.append(lst1[i])
print(lst)
