e = {
    ":)": "🙂",
    ":(": "🙁",
}


def convert(text):
    txt = text.split()
    convert_t = ""

    for tx in txt:
        em = e.get(tx, tx)

        convert_t += em + " "

    return convert_t.strip()

def main():
    i = input("")

    convert_t = convert(i)

    print("", convert_t)

main()