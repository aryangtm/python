f=open('sample.txt','r')
cl=cw=cc=0
for i in f:
    w=i.split()
    cl+=1
    cw+=len(w)
    cc+=len(i)
print('The no of line in file ',cl)
print('The no of words in file',cw)
print('The no of char in file ',cc)
f.close()

