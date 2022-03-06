for i in range(100,1000):
    l=i;sum=0;num=l;
    while l>0:
        r=l%10
        sum=sum+r**3
        l=l//10
    if(num==sum):
        print(num)
