r,c=[int(i)for i in input("Enter size of row and column : ").split()]
for i in range(1,r+1):
    for j in range(1,c+1):
        if ((i==j) and (i!=1 or j!=1) and (i!=r or j!=c)):
            if(i%2!=0 or j%2!=0):
                print("0",end="")
            else :
                print("1",end="")
        else:
                print("1",end="")
    print("\n")            
