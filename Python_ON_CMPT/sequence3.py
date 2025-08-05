i = 1
j = 7

a = 1

while(i < 10):
    print(f"I={i} J={j}")
    a += 1

    j -= 1
    
    if a > 3:
        i += 2
        j = j + 5
        a = 1