n = int(input())
ar = list(map(int,input().strip().split()))
sum = 0
for i in range(0,len(ar)):
	sum += ar[i]
print(sum)