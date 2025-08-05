x = int(input())
c = 0

while c < x:
    a , b = map(int, input().split())

    if b == 0:
        print("divisao impossivel")
    else:
        ans = a / b
        print(f"{ans:.1f}")
    c += 1