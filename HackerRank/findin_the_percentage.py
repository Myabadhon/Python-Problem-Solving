totatl_student = int(input())
marks = {}
for total in range(totatl_student):
    marksheet = input().split(" ")
    marks[marksheet[0]] = marksheet[1:]
quary_name = input()
total_marks = 0
for mark in marks[quary_name]:
    total_marks += float(mark)
average = total_marks / 3
two_decimal = "{:.2f}".format(average)
print(two_decimal)