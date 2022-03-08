r,c=[int(i) for i in input("enter row and column size of pattern : ").split()]
for i in range(1,r+1):
    for j in range(1,c+1):
        if j%2==0:
            print(1,end="")
        else:
         print(0,end="")
    print("\n")    
