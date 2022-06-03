t=int(input())
for i in range(0,t):
    try:
        a,b=[int(i) for i in input().split()]
        print(int(a)//int(b))
    except ZeroDivisionError as e :
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
