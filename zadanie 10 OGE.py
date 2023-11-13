def f(x):
    sum = 0
    while x > 0:
        sum += x % 8  # деление с остатком
        x //= 8  # деление целочисленное
    return sum


print(min(f(86), f(99), f(105)))


def f(x, i):
    x = int(str(x), i)
    return x


print(max(f(36, 16), f(63, 8), f(111100, 2)))

x = int("10000", 2)
print(x)
