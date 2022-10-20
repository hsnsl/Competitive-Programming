#لعبة زوجي فردي
n=int(input())
if(n%2==0):
    print((n-2)//2)
    if((n-2)%4!=0):
        print("Win")
    else:
        print("Lose")
else:
    print((n-1)//2)
    if((n-1)%4!=0):
        print("Win")
    else:
        print("Lose")
