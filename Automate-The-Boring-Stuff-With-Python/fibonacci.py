def fibonacci(n):
    if n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

n = 10
for i in range(n):
    print(fibonacci(i))
# print(fibonacci(10))