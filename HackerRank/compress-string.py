inp = input()
lst =[]
index = 0
x = 1
while index < len(inp):
    item = inp[index]
    for i in range(index + 1, len(inp)):
        if item == inp[i]:
            x += 1
        else:
            break
    lst.append((x,int(item)))
    index += x
    x = 1
print(*lst, sep=" ")