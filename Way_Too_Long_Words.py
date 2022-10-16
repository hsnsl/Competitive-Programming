n=int(input())
a=[]
for i in range(n):
    s = input()
    if(len(s)>10):
        a.append(s[0]+str(len(s)-2)+s[len(s)-1])
    else:
        a.append(s)
for j in range(n):
    print(a[j])
#https://codeforces.com/problemset/problem/71/A
