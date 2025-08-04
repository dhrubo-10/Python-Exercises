def main():
    i = input("What time is it? ")

    h = convert(i)

    if h is not None:
        meal = ""

        if 7.00 <= h <= 8.00:
            meal = "breakfast"

        elif 12.00 <= h <= 13.00:
            meal = "lunch"

        elif 18.00 <= h <= 19.00:
            meal = "dinner"


        if meal:
            print(f"{meal} time")

    else:
        print("Youre not Hungry!")


def convert(time):
    if ":" in time:
        div = time.split(":")
        h = int(div[0])
        m = int(div[1])

    else:
        div = time.split()
        div_t = div[0].split(":")
        h = int(div_t[0])
        m = int(div_t[1])

    if len(div) > 1 and div[1].lower() == "am":
        h += 12

    return h + m / 60.0


if __name__ == "__main__":
    main()