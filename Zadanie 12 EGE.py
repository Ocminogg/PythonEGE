# s = '1' + '0' * 75
# while ('10' in s) or ('1' in s):
#     if '10' in s:
#         s = s.replace('10', '001', 1)
#     else:
#         s = s.replace('1', '00', 1)
#
# print(s.count('0'))

for n in range(1, 100):
    SUM = 0
    s = '3' + (n * '5')
    while ('25' in s) or ('355' in s) or ('555' in s):
        if ('25' in s):
            s = s.replace('25', '3', 1)
        if ('355' in s):
            s = s.replace('355', '52', 1)
        if ('555' in s):
            s = s.replace('555', '23', 1)
    for i in s:
        SUM += int(i)
    if SUM == 27:
        print(n)
        break