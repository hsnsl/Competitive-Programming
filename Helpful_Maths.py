##Examples :
## 1+3+2+5 ----> 1+2+3+5 
## 1+5+10+8+12+9 --> 1+5+8+9+10+12 
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
