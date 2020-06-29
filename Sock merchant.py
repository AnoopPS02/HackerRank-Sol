from collections import Counter
ar = [1, 2, 1, 2, 1, 3, 2]
print(ar)
my_dict = {}
my_dict = Counter(ar)
print(my_dict)
my_list = []
for val in my_dict.values():
	#print(val)
	my_list.append(int(val/2))
print(my_list)
res = 0
for x in my_list:
	res+=x
print(res)

