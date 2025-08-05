def main():
    print(fuel())

def fuel():
    f = ""

    while True:
        fl = flg()

        try:
            x = (fl[0] / fl[1] * 100)

            if x <= 1:
                f = "E"

            elif 1 < x < 99:
                f = f"{round(x)}%"

            elif 99 <= x <= 100:
                f = "F"

            else:
                continue

            break

        except ZeroDivisionError:
            continue

    return f

def flg():
    while True:
        i = input("Fraction: ").split("/")

        try:
            i[0], i[1] = int(i[0]), int(i[1])
            break

        except ValueError:
            continue
    return i

main()