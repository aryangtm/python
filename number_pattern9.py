r,c=[int(i) for i in input("Enter the size of pattern : ").split()]
for i in range(1,r+1):
    for j in range(1,c+1):
        if(i==1 or j==1 or j==c or i==r)and(i!=j and i+j!=r+1):
            print("1",end="")
        else:
            print("0",end="")
    print()
