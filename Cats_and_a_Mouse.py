q = int(input())
for i in range(q):
	cm = list(map(int,input().strip().split()))
	x = cm[0]
	y = cm[1]
	z = cm[2]
	ans1 = abs(x-z)
	ans2 = abs(y-z)
	if ans1 > ans2:
		print("Cat B")
	elif ans2 > ans1:
		print("Cat A")
	else:
		print("Mouse C")