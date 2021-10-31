def print_formatted(number):
    for i in range(number):
        print(f'{i} {oct(i)} {hex(i)} {bin(i)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)