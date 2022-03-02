#Entering teo values from user 

x,y=[int(i) for i in input("Enter two number : ").split()]
#subtarction
c=abs(x-y)
print("Subtraction =",c)
#Addition
a=x+y
print("Addition=",a)
#Multiplication
m=x*y
print("Multiolication=",m)
#Divison
d=x/y
print("Divison =",d)
#Floor Divison
fd=x//y
print("Floor Divison=",fd)
#Power
p=x**y
print("Power of x=%.2f"%p)
