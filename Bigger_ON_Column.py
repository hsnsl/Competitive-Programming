r1,r2,r3=[],[],[]
r1=input().split()
r2=input().split()
r3=input().split()
for i in range(0,3):
    if(int(r1[i])<=1 or int(r1[i]) >= 100 or int(r2[i])<=1 or int(r2[i])>=100 or int(r3[i])<=1 or int(r3[i])>=100):
        print("Numbers should be between 1 and 100")
        exit()
    else:
        r1[i]=int(r1[i])
        r2[i]=int(r2[i])
        r3[i]=int(r3[i])
for i in range(0,3):
    eval('print("The max of the elements of column'+str(i+1)+' :'+'"+str(max(r1['+str(i)+'],r2['+str(i)+'],r3['+str(i)+'])))')

