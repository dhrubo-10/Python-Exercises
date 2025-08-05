while (True):
    x,y = map(int, input().split())
    if x > 0 and y > 0:
        start = min(x,y)
        end = max(x,y)

        sum = 0

        for i in range(start,end + 1):
            sum += i
            print(i, end=" ")
        print(f"Sum={sum}")    
    else:
        break