# s = '1' * 39 + '2' * 39
# while '111' in s:
#     s = s.replace("111", "2", 1)
#     s = s.replace("222", "1", 1)
# print(s)

# for n in range(1, 100):
#     SUM = 0
#     s = '3' + (n * '5')
#     while ('25' in s) or ('355' in s) or ('555' in s):
#         if ('25' in s):
#             s = s.replace('25', '3', 1)
#         if ('355' in s):
#             s = s.replace('355', '52', 1)
#         if ('555' in s):
#             s = s.replace('555', '23', 1)
#     for i in s:
#         SUM += int(i)
#     if SUM == 27:
#         print(n)
#         break

# s = "0" +'1' * 0 + '2' * 3 + "0"
# poisk = "1" *36 + "2" * 30
# for i in range(65):
#     for j in range(65):
#         for t in range(65):
#             s = "0" + ('1' * i) + ('2' * j) + ('3' * t) + "0"
#             while not ('00' in s):
#                 s = s.replace("01", "320", 1)
#                 s = s.replace("02", "2013", 1)
#                 s = s.replace("03", "1210", 1)
#             if s == poisk:
#                 print(s)
s = '1' + '8' * 99 + '1'
while ('81' in s) or ('882' in s) or ('8883' in s):
    if '81' in s:
        s = s.replace('81', '2', 1)
    elif '882' in s:
        s = s.replace('882', '3', 1)
    else:
        s = s.replace('8883', '1', 1)
print(s)