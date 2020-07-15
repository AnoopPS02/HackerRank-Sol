ar = list(map(int,input().strip().split()))
min1 = min(ar)
max1 = max(ar)
minsum = 0
maxsum = 0
if min1 == max1:
    for i in range(1,len(ar)):
        minsum+=ar[i]
    maxsum = minsum
else:
    for i in range(0, len(ar)):
        if ar[i] == min1:
            pass
        else:
            maxsum += ar[i]
    for i in range(0, len(ar)):
        if ar[i] == max1:
            pass
        else:
            minsum += ar[i]
print(minsum,maxsum)