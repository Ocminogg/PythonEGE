def f(x, y, h):
    if (h == 3 or h == 5) and x + y >= 151:
        return 1
    elif h == 5 and x + y < 151:
        return 0
    elif x + y >= 151 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 4, y, h + 1) or f(x, y * 4,
                                                                                       h + 1)  # стратегия победителя
        else:
            return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and f(x * 4, y, h + 1) and f(x, y * 4,
                                                                                          h + 1)  # сратегия проигравшего(любой ход)


def f1(x, y, h):
    if h == 3 and x + y >= 151:
        return 1
    elif h == 3 and x + y < 151:
        return 0
    elif x + y >= 151 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, y, h + 1) or f1(x, y + 1, h + 1) or f1(x * 4, y, h + 1) or f1(x, y * 4,
                                                                                           h + 1)  # стратегия победителя
        else:
            return f1(x + 1, y, h + 1) and f1(x, y + 1, h + 1) and f1(x * 4, y, h + 1) and f1(x, y * 4,
                                                                                              h + 1)  # стратегия проигравшего(любой ход)


for x in range(1, 142):
    if f(x, 9, 1) == 1:
        print(x)
print("====")
for x in range(1, 142):
    if f1(x, 9, 1) == 1:
        print(x)