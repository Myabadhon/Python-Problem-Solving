n = int(input())
x = [int(x) for x in input().split()]
x.sort()
max = x[0]
for number in x:
    if number > max:
        max = number
print(x[(x.index(max))-1])