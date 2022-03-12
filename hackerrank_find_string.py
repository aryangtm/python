def count_substring(s, ss):
    x=len(s)
    y=len(ss)
    c=0
    for i in range(0,x):
        if(s[i:i+y]==ss[::]):
            c+=1               
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
