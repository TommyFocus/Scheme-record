a = 0

for i in range(100, 1000):
    for j in str(i):
        a += int(j) ** 3
    if a == i:
        print(i)
    a = 0

print("------------------")
for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            num = x*100 + y*10 + z
            tmp = x**3 + y**3 + z**3
            if num == tmp:
                print(num)

print('cheng fa kou jue')

for i in range(1, 10):
    for j in range(1, i+1):
        print(i, '*', j, '=', i * j)
