# s = ""
# for i in range(60, 100):
#     s = "1" * i
#     while '111' in s:
#         s = s.replace("111", "2", 1)
#         s = s.replace("222", "1", 1)
#     if s == "221":
#         print(i)


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
# s = '1' + '8' * 99 + '1'
# while ('81' in s) or ('882' in s) or ('8883' in s):
#     if '81' in s:
#         s = s.replace('81', '2', 1)
#     elif '882' in s:
#         s = s.replace('882', '3', 1)
#     else:
#         s = s.replace('8883', '1', 1)
# print(s)

# for x in range(60):
#     for y in range(60):
#         for z in range(60):
#             s = "0" + ("1" * x) + ("2" * y) + ("3" * z)
#             start = s
#             while ('01' in s) or ('02' in s) or ('03' in s):
#                 s = s.replace('01', '30', 1)
#                 s = s.replace('02', '101', 1)
#                 s = s.replace('03', '202', 1)
#             if s.count("1") == 15 and s.count("2") == 10 and s.count("3") == 60:
#                 print(start.count("1"))
#                 break

# s = 127 * "9"
# while "333" in s or "999" in s:
#     if "333" in s:
#         s = s.replace("333", "9", 1)
#     else:
#         s = s.replace("999", "3", 1)
# print(s)

# s = "1" * 10
# for i in range(20):
#     s = s.replace("1", "12", i)
#     print("Start ", s)
#     while "12" in s:
#         s = s.replace("12", "4", 1)
#     SUM = 0
#     for i in s:
#         SUM += int(i)
#     print(SUM)
#     print("End ", s)
#     s = "1" * 10

# s = "2" + "8" * 99 + "2"
# while ("81" in s) or ("882" in s) or ("8883" in s):
#     if ("81" in s):
#         s = s.replace("81","2",1)
#     elif ("882" in s):
#         s = s.replace("882","3",1)
#     else:
#         s = s.replace("8883","1",1)
# print(s)
# def Simple(s):
#     #сумма цифр строки
#     SUM = 0
#     for i in s:
#         SUM += int(i)
#     # проверка простых чисел
#     for Del in range(2, SUM//2):
#         if SUM % Del == 0:
#             return False
#     return True
#
# s = ''
# for n in range(40,100):
#     s = '0' + '1'*40 + '2' * n + '0'
#     while '00' not in s:
#         s = s.replace("02", "101",1)
#         s = s.replace("11", "2",1)
#         s = s.replace("012", "30",1)
#         s = s.replace("010", "00",1)
#     if Simple(s):
#         print(s)
#         print(n)
#         break


