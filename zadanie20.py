def f(x, y, h):
    if h == 4 and (x >= 48 or y >= 48):
        return 1
    elif h == 4 and (x < 48 or y < 48):
        return 0
    elif (x >= 48 or y >= 48) and h < 4:
        return 0
    else:
        if h % 2 != 0:
            if max(x, y) == x:
                if x != y:
                    return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x + 3, y, h + 1) or f(x, y * 2, h + 1)  # стратегия проигравшего
                else:
                    return f(x + 1, y, h + 1) or f(x + 2, y, h + 1) or f(x + 3, y, h + 1)
            if max(x, y) == y:
                if x != y:
                    return f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y + 3, h + 1) or f(x * 2, y, h + 1)  # стратегия проигравшего
                else:
                    return f(x, y + 1, h + 1) or f(x, y + 2, h + 1) or f(x, y + 3, h + 1)
        else:
            if max(x, y) == x:
                if x != y:
                    return f(x + 1, y, h + 1) and f(x + 2, y, h + 1) and f(x + 3, y, h + 1) and f(x, y * 2, h + 1)  # стратегия проигравшего
                else:
                    return f(x + 1, y, h + 1) and f(x + 2, y, h + 1) and f(x + 3, y, h + 1)
            if max(x, y) == y:
                if x != y:
                    return f(x, y + 1, h + 1) and f(x, y + 2, h + 1) and f(x, y + 3, h + 1) and f(x * 2, y, h + 1)  # стратегия проигравшего
                else:
                    return f(x, y + 1, h + 1) and f(x, y + 2, h + 1) and f(x, y + 3, h + 1)


for x in range(1, 48):
    if f(x, 13, 1) == 1:
        print(x)

