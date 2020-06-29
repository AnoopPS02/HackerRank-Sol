n = input()
keyboards = input()
usb = input()
lst1 = n.split(" ")
kb = keyboards.split(" ")
drives = usb.split(" ")
for i in lst1:
    b = int(lst1[0])
for j in range(0,len(kb)):
    kb[j] = int(kb[j])
for k in range(0,len(drives)):
    drives[k] = int(drives[k])
sum1 = []
for x in range(0,len(kb)):
    for y in range(0,len(drives)):
        sum1.append(kb[x]+drives[y])
final = []
for z in range(0,len(sum1)):
    if sum1[z] <= b:
        final.append(sum1[z])
    else:
        final.append(-1)
print(max(final))