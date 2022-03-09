r,c=[int(i) for i in input("Enter size of row and column : ").split()]
for i in range(1,r+1):
    for j in range(1,c+1):
        if(i==r//2+1 or j==c//2+1):
            print("0",end="")
        else :
            print("1",end="")
    print("\n")
