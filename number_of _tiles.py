l,w=[int(i)for i in input("Enter length and widhth of room:").split()]
l1,w1=[int(i) for i in input("Enter length and width of tile:").split()]
ar=l*w
at=l1*w1
nt=ar//at
print("Number of tiles=",nt)
