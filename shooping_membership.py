a=int(input("Enter the amount : "))
if a>=25000:
    print("You are GOLD member")
    p=a-a*0.2
    print("You have to pay : %d"%p)
elif a>10000 and a<25000:
    print("You are SILVER member")
    p=a-a*0.1
    print("You have to pay : %d"%p)
else:
    print("You are BRONZE member")
    p=a-a*0.05
    print("You have to pay : %d"%p)
