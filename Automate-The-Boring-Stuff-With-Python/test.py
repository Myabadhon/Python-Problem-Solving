# import textwrap as tr
# lst = "Hellodearhow are you"
# lst = tr.wrap(lst, width=4)
# print(*lst, sep="\n")
# print(lst)
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    # string, max_width = input(), int(input())
    result = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)
    print(result)