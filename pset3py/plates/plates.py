c = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "X", "Z"]
n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    elif chckr(s):
        return False

    elif chcks(s):
        return False

    elif chckz(s):
        return False

    elif chcka(s):
        return False
    else:
        return True

def chckr(s):
    for a in s:
        if not(a in c or a in n):
            return True

def chcks(s):
    for a in s[:2]:
        if not a in c:
            return True

def chckz(p):
    l = len(p)
    position = 0
    number = 0
    z = None

    if any (a in n for a in p):
        for a in p[0:l]:
            if a == "0":
                z = position
                break
            position += 1
        for a in p[0:z]:
            if a in n:
                number = 1
        if number == 0:
            return True

        else:
            return False

def chcka(p):
    l = len(p)
    position = 0
    nmb = None

    if any(a in n for a in p):
        for a in p[0:l]:
            if a in n:
                nmb = position
                break
            position += 1
        for a in p[nmb:l]:
            if a in c:
                return True

    else:
        return False

main()