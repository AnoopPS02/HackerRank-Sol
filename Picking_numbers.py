n =  int(input())
ar = list(map(int,input().strip().split()))
maximum = 0
diff = 1
for k in ar:
	print(k)
	n1 = ar.count(k)
	n2 = ar.count(k-diff)
	maximum = max(maximum,n1+n2)
print(maximum)
