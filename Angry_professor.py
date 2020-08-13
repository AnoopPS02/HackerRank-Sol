def prof(n_k,ar):
	studCount = 0
	for i in ar:
		if i <= 0:
			studCount += 1
		else:
			pass
	return studCount

t = int(input())
for _ in range(t):
	n_k = list(map(int,input().strip().split()))
	ar = list(map(int,input().strip().split()))
	count1 = prof(n_k,ar)
	if count1 >= n_k[1]:
		print('Yes')
	else:
		print('No') 
