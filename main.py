N = int(input())
count = 0
for i in range(N):
    x = int(input())
    if x % 3 == 0:
        count += 1
print(count)