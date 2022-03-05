t=int(input())
v=15*t
if v==785:
    print("The water tank is full,turn off the pump. Thank you!")
elif v>785:
    print("Overflow")
    print(""%.1f'%(v-785))
elif v<785:
    print("Underflow")
    h=v/78.5
    print('%.2f'%h)
    print('%.2f'%(10-h))
