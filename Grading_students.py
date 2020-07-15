import math
n = int(input())
marks = []
for i in range(n):
	inp = int(input())
	marks.append(int(inp))
for j in range(0,len(marks)):
	if marks[j] < 38:
		print(marks[j])
	else:
		rem = marks[j] % 5
		if rem < 3:
			print(marks[j])
		else:
			print(round(marks[j]/5)*5)
