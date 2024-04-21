# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and w) or (w and z)) == ((z <= y) and (y <= x)):
#                     print(x, y, z, w)  # Вывод программы
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and not y) or (y == z) or not w) == 0:
                    print(x, y, z, w)


# a = 5
# b = "Привет Мир!\n"
# # t = a // b
# print(b*a)

# for i in range(4):
#     # print(i)
#     word = "dog"
#     print(word)

#
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 print(x, y, z, w)

# for i in range(2):
#     for j in range(2):
#         for z in range(2):
#             for x in range(2):
#                 print(i,j,z,x)
# A = [12, 33, 111, -232, 11123]
# print(A[4])
# for x in A:
#     print(x)
# for i in range(5):
#     print(A[i])
# for i in range(len(A)):
#     print(A[i])
