def swap(a , b):
    temp = a
    a = b
    b = temp
    return a , b

def singleline(x, y):
    y, x = x, y
    return x,y

def swap_function(a, b):
    return swap(a,b)

print(swap(5,10))
print(singleline(15, 20))
print(swap_function(50, 100))