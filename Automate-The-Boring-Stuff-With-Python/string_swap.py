def swap_case(a):
    listt = []
    for i in a:
        if i == i.upper():
            b = i.lower()
            listt.append(b)
        else:
            b = i.upper()
            listt.append(b)
    empty = "".join(listt)
    return empty
a = input()
print(swap_case(a))