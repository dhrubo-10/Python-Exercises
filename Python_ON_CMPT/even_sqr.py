a = int(input())

for i in range(1, a+1):
    if i % 2 == 0:
        sqr = i * i
        print(f"{i}^2 = {sqr}")