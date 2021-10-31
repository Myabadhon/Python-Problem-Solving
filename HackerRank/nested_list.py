list1 = [[input(), float(input())] for _ in range(int(input()))]
scores = sorted({s[1] for s in list1})
result = sorted(s[0] for s in list1 if s[1] == scores[1])
print('\n'.join(result))