i=1
f=0
x=int(input("Enter number : "))
while(i<x):
    if(x%i==0):
        f=f+i
    i=i+1

if(f==x):
    print("Perfect number")
else:
    print("Not Perfect number")
