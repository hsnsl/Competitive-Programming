def swap_case(s):
    r=''
    a=list(s)
    for i in range(0,len(s)):
        if(a[i]==a[i].upper()):
            a[i]=a[i].lower()
        else:
            a[i]=a[i].upper()
    for j in range(len(a)):
        r=r+a[j]
    return r
s = input()
result = swap_case(s)
print(result)
