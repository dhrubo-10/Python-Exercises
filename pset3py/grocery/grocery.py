list = {}

while True:
    try:
        i = input().upper()

        if i in list:
            list[i] += 1

        else:
            list[i] = 1

    except EOFError:
        for k in sorted(list.keys()):
            print(list[k], k)
        break