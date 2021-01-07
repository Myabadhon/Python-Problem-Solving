salary = float(input())

if salary >= 0 and salary <= 2000.00:
    tax = " Isento"
elif salary >= 2000.01 and salary <= 3000.00:
    salary1 = salary - 2000.00
    temp_salary = (salary - 2000.00)-salary1
    print(salary1)
    print(temp_salary)
    # tax1 = ((8 / 100) * 1000)
elif salary >= 3000.01 and salary <= 4500.00:
    tax = ((18/ 100) * salary)
elif salary >= 4500.00:
    tax = ((28/100) * salary)
# print("R$ %.2f"%tax)
# print("R$ {}".format(tax))
