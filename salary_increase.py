salary = float(input())

if salary > 0 and salary <= 400:
    temp_salary=((15/100)*salary)
    salary = temp_salary+salary
    percent = 15
elif salary >= 400.01 and salary <= 800:
    temp_salary=((12/100)*salary)
    salary = temp_salary+salary
    percent = 12
elif salary >= 800.01 and salary <= 1200:
    temp_salary=((10/100)*salary)
    salary = temp_salary+salary
    percent = 10
elif salary >= 1200.01 and salary <= 2000:
    temp_salary = ((7 / 100) * salary)
    salary = temp_salary + salary
    percent = 7
elif salary > 2000:
    temp_salary=((4/100)*salary)
    salary = temp_salary+salary
    percent = 4

print("Novo salario : {:.2f}".format(salary))
print("Reajuste ganho : {:.2f}".format(temp_salary))
print("Em percentual : "+str(percent)+" %")
