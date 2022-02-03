loop = 1000000
a = 0
b = 1
for i in range(1, loop, 1):
    a = a + b
    b = a - b
    print(a)
