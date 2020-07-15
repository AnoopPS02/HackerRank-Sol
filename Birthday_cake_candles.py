n = int(input())
ar = list(map(int,input().strip().split()))
max1 = max(ar)
count = 0
for i in range(0,len(ar)):
    if ar[i] == max1:
        count+=1
    else:
        pass
print(count)