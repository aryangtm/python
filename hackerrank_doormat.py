n,m=[int(i) for i in input().split()]
c='.|.'
for i in range(n//2):
    print((c*(2*i+1)).center(m,'-'))
print(('WELCOME').center(m,'-'))
for i in range(n//2,0,-1):
    print((c*(2*i-1)).center(m,'-'))
