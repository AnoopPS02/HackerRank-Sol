def rev(n):
	rev = 0
	while(n > 0):
		a = n % 10
		rev = rev * 10 + a 
		n = n // 10
	return rev

ijk = list(map(int,input().strip().split()))
i = ijk[0]
j = ijk[1]
k = ijk[2]
days_count = 0
for n in range(i,j+1):
	rev_n = rev(n)
	n = abs(n-rev_n)
	if n%k == 0:
		days_count += 1
print(days_count)