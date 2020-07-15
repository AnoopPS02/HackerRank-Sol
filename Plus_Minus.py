n = int(input())
ar = list(map(int,input().strip().split()))
pos = 0
neg = 0
zero = 0
for i in range(0 , len(ar)):
    if ar[i]>0:
        pos+=1
    elif ar[i]<0:
        neg+=1
    else:
        zero+=1
print('%6f'%(pos/n))
print('%6f'%(neg/n))
print('%6f'%(zero/n))