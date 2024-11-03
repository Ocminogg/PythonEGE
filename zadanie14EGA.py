# for x in '012345678':
#     for y in '012345678':
#         t = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
#         if t % 61 == 0:
#             print(t // 61)
#             break


# for x in '0123456789ABCDE':
#     t = int('123' + x + '5', 15) + int('1' + x + '233', 15)
#     if t % 14 == 0:
#         print(t//14)
#         break


# S = min(result_search)
# S = S//61
# print(S)
#
# r = int('AF24', 16)
# print(r)

# E = False
# T = ''
# S = 49**10 + 7**20 - 49
# while S != 0:
#     T = T + str(S % 7)
#     S = S // 7
# print(T.count("6"))

# print(bin(4**511 + 2**511 - 511).count("1"))

# for x in range(5):
#     print(x)

# for x in '0123456789ABC':
#     for y in '0123456789ABC':
#         t = int("8" + x + "78" + y, 13) + int('79' + x + y + '7', 18)
#         if t % 9 == 0:
#             print(t // 9)
#             break
#     if t % 9 == 0:
#         break


# A = ["0","1","2","3","4","5","6","7","8",]
# for x in A:
#     for y in '012345678':
#         if (int("88" + x + "4" + y,9) + int("7" + x + "44" + y,11)) % 61 == 0:
#             print((int("88" + x + "4" + y,9) + int("7" + x + "44" + y,11)) // 61)



# for x in '0123456789ABC':
#     for y in '0123456789ABC':
#         t = int("8" + x + '78' + y, 13) + int("79" + x + y + '7', 18)
#         if t % 9 == 0:
#             print(t // 9)
#             break

# result_search = []
# for x in '0123456789A':
#     for y in '0123456789A':
#         t = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
#         if t % 305 == 0:
#             result_search.append(t)
# print(min(result_search) // 305)

# print(122**0.5)
# print(int(122**0.5))
# if 122**0.5 != int(122**0.5):
#     print("False")
# print((122**0.5)**2 )

# for x in range(39):
#     for y in range(39):
#         t = 5*39**8+8*39**7+x*39**6+7*39**5+2*39**4+3*39**3+y*39**2+4*39*1+9
#         if t % 38 == 0 and (y * 39 ** 1 + x) ** 0.5 == int((y * 39 ** 1 + x) ** 0.5):
#             print(y * 39 ** 1 + x)

# s = ''
# for x in range(20):
#     for y in range(20):
#         s = str(x) + str(y) + '2'

# for p in range(100):
#     for x in range(p):
#         for y in range(p):
#             s = (3 * p + 2) * (p + 4)
#             r = x * p ** 2 + y * p + 2
#             if s == r:
#                 print(y * p + x)
# print((3*2**23)/(1080*920*0.8))
#
#
# i=20
# L=3*2**23/0.8
# k=1080*920
# print(L/k-i)
# print(oct(10)[2:] + " это двоичный код 10")
SUM = 0
for x in range(13):
    SUM = (15**3 * 4 + 15**2 * 12 + 15 * x + 4) + (13**3 * x + 13**2 * 6 + 13 * 2 + 10)
    if SUM % 121 == 0:
        print(SUM / 121)
        print(x)

