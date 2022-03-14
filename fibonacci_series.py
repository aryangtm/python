a,b=0,1
sum=0
n=int(input("Enter the range : "))
print(a    ,b,end="\t")
while(n>2):
    sum=a+b
    a=b
    b=sum
    n=n-1
    print(sum,end=" \t")
    
