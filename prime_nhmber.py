x=int(input())
i=1
c=0
for i in range(1,x+1,1):
    if x%i==0:
        c+=1

if c==2:
    print("Prime number")
else:
    print("Not prime number")           
    
