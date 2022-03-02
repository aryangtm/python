a,b,c=[int(i) for i in input("Enter the sides of triangle:").split()]
if a!=b!=c:
    print("Scalene traingle ")
elif (a==b)|(a==c)|(b==c):
    print('Isosceles triagnle')
elif a*a==(b*b)+(c*c):
    print("Right angled triangle")
elif (a+b>c)|(a+c>b)|(b+c>a):
    print("Invalid triangle")
    
