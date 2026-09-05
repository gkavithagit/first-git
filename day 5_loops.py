for i in range(5):
    print(i)

for i in range(1,11):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(1,6):
    print(i * 2)

for i in range(1,11):
    print(5 * i)

i = 1
while i <= 5:
    print(i)
    i = i+1

for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,6):
    if i == 3:
        continue
    print(i)

for i in range(3):
    for j in range(2):
        print(i,j)