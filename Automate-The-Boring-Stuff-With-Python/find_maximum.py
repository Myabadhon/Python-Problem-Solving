def find_maximum(numbers):
    maximum = numbers[0]
    for  number in numbers:
        if number > maximum:
            maximum = number
    return maximum

numbers = [5, 2, 6, 9, 10, 11, 22, 50, 80, 90, 100, 55, 8, 1]

print(find_maximum(numbers))