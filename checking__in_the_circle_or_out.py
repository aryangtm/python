x,y=[int(i) for i in input("Enter the center of circle: ").split()]
x1,y1=[int(i)for i in input("Enter an arbitary point: ").split()]
r=int(input("Enter radius: "))
c=(((x1-x)**2)+((y1-y)**2))**(1/2)
if c<=r:
    print("In the circle")
else:
    print("Out the circle")
