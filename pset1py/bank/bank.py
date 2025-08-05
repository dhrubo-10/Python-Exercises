def main():
    greet = input("Greetings: ")
    gr = greet.strip().capitalize()
    fword = greet.strip().lower()


    if gr.startswith("Hello"):
        print("$0")

    elif fword.startswith("h"):
        print("$20")

    else:
        print("$100")

main()