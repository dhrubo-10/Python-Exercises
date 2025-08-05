n = int(input())


for _ in range(n):
    x, y = map(int, input().split())


        
    start = min(x, y)
    end = max(x, y)
    
    total = []

    for j in range(start + 1, end):
        if j % 2 != 0:
            total.append(j)
    t = sum(total)
    print(t)
