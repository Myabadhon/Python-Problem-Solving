n = int(input())
lists = input().split()
lists = [int(i) for i in lists]
if n == len(lists):
    t = tuple(lists)
    print(hash(t))