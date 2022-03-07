x,y=[int(i) for i in input("Enter strating and ending point : ").split()]
for j in range(x,y+1):
    i=1
    c=0
    for i in range(1,j+1,1):
        if j%i==0:
            c+=1
    if c==2:
        print(j)      
    
