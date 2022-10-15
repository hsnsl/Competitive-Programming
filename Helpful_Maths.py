s=input() 
ar=s.split('+') 
l=len(ar)
ar.sort()
p=""
for i in range(l):
    p=p+ar[i]
    if(i!=l-1):
        p=p+"+"
print(p)
