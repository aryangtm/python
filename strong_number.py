n=int(input())
f=1;sum=0;l=n
while(n>0):
    r=n%10
    n=n//10
    while(r>0):
        f=f*r
        r=r-1
    sum=sum+f
    f=1
if(l==sum):
    print("Strong number")
else:
    print("Not strong number")
