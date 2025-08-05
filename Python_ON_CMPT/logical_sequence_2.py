x,y = map(int, input().split())

c = int(y/x) + 1

count = 1

for i in range(1, c):
    r = ""
    for j in range(x):
        r += str(count) + " "
        count += 1

    print(r[:-1])

    