def main():
    c_case = input("camelCase: ")
    s_case = cs(c_case)
    print("snake_case", s_case)

def cs(camelCase):
    snake_case = []
    x = ""

    for word in camelCase:
        if word.isupper() and x.isalnum():
            snake_case.append("_")
        snake_case.append(word.lower())

        x = word

    return "".join(snake_case)
main()