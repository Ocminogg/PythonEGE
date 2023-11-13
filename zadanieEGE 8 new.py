import itertools

words = itertools.product("ДЕМЬЯН", repeat=5)
for i in words:
    word = ''.join(i)
    print(word)
