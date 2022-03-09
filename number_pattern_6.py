r,c=[int(i) for i in input("Enter the size of row and column :").split()]
for i in range(1,r+1):
    for j in range(1,c+1):
        if(i==j):
           print("1",end="")
        elif(i%2!=0 and j%2!=0):
            print("1",end="")
        elif(i%2!=0 and j%2==0):
            print("0",end="")
        elif(i%2==0):
            if(j%2!=0):
                print("0",end="")
            else:
                print("1",end="")
    print("\n")
        
