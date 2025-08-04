def main():
    i = input("Input: ")

    wv = rv(i)

    print(f"Output: {wv}")

def rv(text):
    v = "aeiouAEIOU"
    wv = ""

    for t in text:
        if t not in v:
            wv += t

    return wv

main()

