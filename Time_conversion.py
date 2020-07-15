inp = input()
if inp[-2:] == 'AM' and inp[:2] == "12":
    print("00"+inp[2:-2])
elif inp[-2:] == 'PM' and inp[:2] == "12":
    print(inp[:-2])
elif inp[-2:] == 'AM':
    print(inp[:-2])
else:
    print(str(int(inp[:2])+12)+inp[2:-2])