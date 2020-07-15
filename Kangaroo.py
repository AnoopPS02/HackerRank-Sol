def kang(x1,v1,x2,v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"   
ar = list(map(int,input().strip().split()))
x1 = ar[0]
v1 = ar[1]
x2 = ar[2]
v2 = ar[3]
ans = kang(x1,v1,x2,v2)
print(ans)