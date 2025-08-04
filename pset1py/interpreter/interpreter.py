def intp(x,y,z):
    if y == "+":
        return x + z

    elif y == "-":
        return x - z

    elif y == "*":
        return x * z

    elif y == "/":
        return x / z

def main():
    i = input("Expressions: ")
    x,y,z = i.split()

    x = int(x)
    z = int(z)

    if y not in ["+", "-", "*", "/"]:
        print("Invalid Operator")
        return

    if y == "/" and z == 0:
        print("Math Error!")

        return

    inter = intp(x,y,z)
    r = "{:.1f}".format(inter)

    print(r)

main()
