def f(x, h):
    if h == 4 and x >= 68:
        return 1
    elif h == 4 and x < 68:
        return 0
    elif x >= 68 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)  # стратегия победителя
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)  # стратегия проигравшего

for x in range(1, 68):
    if f(x, 1) == 1:
        print(x)