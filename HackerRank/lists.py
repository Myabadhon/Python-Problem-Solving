lists = []
n = int(input())

for _ in range(n):
    command = input().split(" ")
    if command [0] == "insert":
        lists.insert(int(command[1]), int(command[2]))
    elif command[0] == "remove":
        lists.remove(int(command[1]))
    elif command[0] == "append":
        lists.append(int(command[1]))
    elif command[0] == "sort":
        lists.sort()
    elif command[0] == "pop":
        lists.pop()
    elif command[0] == "reverse":
        lists.reverse()
    else:
        print(lists)