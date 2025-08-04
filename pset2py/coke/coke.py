print("Amount Due: 50")
coins = 0

while coins < 50:
    c = int(input("Insert coin: "))

    if c == 5 or c == 10 or c == 25:
        coins += c

        amount = 50 - coins

        if amount <= 0:
            x = coins - 50

            print(f"Change Owed: {x}")
            break

        else:
            print(f"Amount Due: {amount}")

    else:
        print("Amount Due: 50")