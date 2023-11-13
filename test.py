x = bin(59)
print(x)
y = bin(71)
print(y)
z = bin(81)
print(z)


A = []
sum = 0
for i in range(3):
    x = int(input())
    while x != 0:
        sum += x % 2
        x = x // 2
    A.append(sum)
    sum = 0
print(min(A))

print("Hello Artem")