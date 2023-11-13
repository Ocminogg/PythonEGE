x = 10
y = 382
print(y % x)
y = y//x
print(y % x)


x = 382
y = 123
if x > y:
    print("x > y")
elif x == y:
    print("x = y")
else:
    print("x < y")


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(str(x)+str(y)+str(z))

for x in range(-3,10):
    print(x)

print("\n")
for x in range(-3,10,3):
    print(x)
print("\n")

A = [10,20,-2334,1230,0]
print(A[0])
print(A[2])
print("\n")

for i in A:
    print(i)

print("\n")

for i in range(len(A)):
    print(A[i])