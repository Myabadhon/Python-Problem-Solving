list1 = [1,2,2,3,4,5,5,6,7]
uniques = []
for item in list1:
    if item not in uniques:
        uniques.append(item)
print(uniques)