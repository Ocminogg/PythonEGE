def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 2, y) + f(x * 3, y) + f(x * 4, y)
print(f(1, 59) * f(59, 68) * f(68, 77) * f(77, 86) * f(86, 95) * f(95,600))

# print(f(1, 59) * f(59, 68) * f(68, 77) * f(77, 86) * f(86, 95) * f(95,600))

def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(2, 15) * f(15, 30))