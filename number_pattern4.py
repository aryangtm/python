r,c=[int(i) for i in input("enter row and column size of pattern : ").split()]
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or j==1:
            print(1,end="")
        elif i==r or j==c:
            print(1,end="")
        else:
         print(0,end="")
    print("\n")    
