r,c=[int(i) for i in input("enter row and column size of pattern : ").split()]
for i in range(1,r+1):
    for j in range(1,c+1):
        if i%2==0:
            print(0,end="")
        else:
         print(1,end="")
    print("\n")    
