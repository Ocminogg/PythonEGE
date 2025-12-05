# x = 1
# SUM = 0
# count = 0
# while x != 0:
#     x = int(input())
#     if x % 8 == 0 and x != 0:
#         SUM += x
#         count += 1
# if count == 0:
#     print("NO")
# else:
#     print(SUM/count)
count = 0
count = 0
for x in range(10,100):
    if ((x >= 47) and not((x % 4 == 0) and not(x % 8 == 0))) == 0:
        count += 1
print(count)