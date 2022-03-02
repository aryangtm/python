n=int(input("Enter rupees :"))

tt=n//2000
n=n%2000
fh=n//500
n=n%500
th=n//200
n=n%200
h=n//100
n=n%100
f=n//50
n=n%50
tw=n//20
n=n%20
t=n//10
n=n%10
five=n//5
n=n%5
one=n//1
n=n%1
Total=tt+fh+th+h+f+tw+t+five+one
print("Notes of 2000:",tt)
print("Notes of 500:",fh)
print("Notes of 200:",th)
print("Notes of 100:",h)
print("Notes of 50:",f)
print("Notes of 20:",tw)
print("Notes of 10:",t)
print("Notes of 5:",five)
print("Notes of 1:",one)
print("Total number of notes:",Total)
