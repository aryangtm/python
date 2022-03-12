if __name__ == '__main__':
    s = input()
    a=b=c=d=0
    for i in range(0,len(s)):
        if('a'<=s[i] and s[i]<='z'):
            a=1
        elif('A'<=s[i] and s[i]<='Z'):
            b=1
        elif('0'<=s[i] and s[i]<='9'):
            c=1
        else :
            d=1
    print(a==1 or b==1 or c==1)
    print(a==1 or b==1)
    print(c==1)
    print(a==1)
    print(b==1)    
