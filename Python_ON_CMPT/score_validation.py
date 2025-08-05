count = 0
s = 0
while True:
    x = float(input())

    if x < 0 or x > 10:
        print("nota invalida")

    elif x > 0 or x < 10:
        s += x
        count += 1
    if count == 2:
        avg = s / 2
        print(f"media = {avg:.2f}")
        break