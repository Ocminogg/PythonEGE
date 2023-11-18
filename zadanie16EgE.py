# def F(n):
#     if n == 0:
#         return 3
#     if 0 < n and n <= 15:
#         return F(n-1)
#     if 15 < n and n < 100:
#         return 2.5 * F(n-3)
#     if n >= 100:
#         return 3.3 * F(n-2)
# print(F(100))


# def F(n):
#     if n == 0:
#         return 0
#     if n % 2 == 1:
#         return F(n - 1) + 1
#     if (n > 0) and (n % 2 == 0):
#         return F(n/2)

# count = 0
# for i in range(1000000000):
#     if F(i) == 2:
#         count += 1
#     print(count)
# print(count)

# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2*G(n-1)+5*n
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1)+2*n
# print(F(4) + G(4))

def F(n):
    if n == 1:
        return 1
    if n % 2 != 0 and n > 1:
        return n + F(n - 2)
    if n % 2 == 0:
        return n * F(n - 1)

print(F(40))