count = 0
s = 0
ans = 1

while ans == 1:
    x = float(input())

    if x < 0 or x > 10:
        print("nota invalida")

    elif x > 0 or x < 10:
        s += x
        count += 1
    if count == 2:
        avg = s / 2
        print(f"media = {avg:.2f}")
        
        ans = 0
        while ans not in (1, 2):
            print("novo calculo (1-sim 2-nao)")
            ans = int(input())

        if ans == 1:
            count = 0
            s = 0
        elif ans == 2:
            break