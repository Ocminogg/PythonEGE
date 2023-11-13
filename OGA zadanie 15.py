x = 1
SUM = 0
count = 0
while x != 0:
    x = int(input())
    if x % 8 == 0 and x != 0:
        SUM += x
        count += 1
if count == 0:
    print("NO")
else:
    print(SUM/count)
