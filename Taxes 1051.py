salary = float(input())

# salary = float(salary-2000.00)
if salary >= 0 and salary <= 2000.00:
    tax = " Isento"
elif salary >= 2000.01 and salary <= 3000.00:
    tax = ((8 / 100) * salary)
elif salary >= 3000.01 and salary <= 4500.00:
    tax = ((18/ 100) * salary)
elif salary >= 4500.00:
    tax = ((28/100) * salary)
# print("R$ %.2f"%tax)
print("R$ {}".format(tax))
