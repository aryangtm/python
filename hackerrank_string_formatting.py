def print_formatted(n):
    l=len(str(bin(n)))-2
    for i in range(1,n+1):
     a=str(i)
     x=str(oct(i))[2:]
     y=str(hex(i))[2:].upper()
     z=str(bin(i))[2:]
     print(a.rjust(l),x.rjust(l),y.rjust(l),z.rjust(l))
     
     

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
