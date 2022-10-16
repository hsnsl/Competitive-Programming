n=int(input())
c=0
for i in range(n):
    o=0
    s=input()
    a=s.split(' ')
    for j in range(3):
        if((a[j])=='1'):
            o+=1
    if(o>1):
        c+=1
print(c)
#https://codeforces.com/problemset/problem/231/A
