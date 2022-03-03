n=int(input("Enter number of apple : "))
if (n%7==0):
	if((n%6==1)and(n%5==1)and(n%4==1)and(n%3==1)and(n%2==1)):
		g=n%7
		g1=g*7
		a=n%6
		a1=a*6
		b=n%5
		b1=b*5
		c=n%5
		c1=c*5
		d=n%4
		d1=d*4
		e=n%3
		e1=e*3
		f=n%2
		f1=f*2
		nn=g1+a1+b1+c1+d1+e1+f1
		print("No of pair of apple =%d"%nn)
else :
	print("Condition Mismatched")

