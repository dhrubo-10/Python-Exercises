while True:
    x = int(input())

    if x == 0:
        break

    output = ""

    for j in range(1,x+1):
        output += str(j) + " "
    print(output[:-1])