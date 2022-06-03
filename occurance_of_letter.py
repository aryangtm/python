x=input()
d={}
for i in x:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    print('Key={}\t Its occurance={}'.format(k,v))
