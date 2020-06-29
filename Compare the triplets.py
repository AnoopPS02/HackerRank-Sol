alice = list(map(int,input().rstrip().split()))
bob = list(map(int,input().rstrip().split()))
a_score = 0
b_score = 0
res = []
for i in range(0 , len(alice)):
	if alice[i]>bob[i]:
		a_score+=1
	elif alice[i]<bob[i]:
		b_score+=1
	else:
		pass
res.append(a_score)
res.append(b_score)
print(res[0] , res[1])
