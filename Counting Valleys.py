n = int(input())
inp = input().strip()
sea_level = 0
valley = 0
for i in inp:
	if i == 'U':
		sea_level += 1
	elif i == 'D':
		sea_level -= 1
	if sea_level == 0:
		if prev < sea_level:
			valley += 1
	prev = sea_level
print(valley)
