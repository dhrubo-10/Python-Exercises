n = int(input())

avg = []

for i in range(n):
    a, b, c = map(float, input().split())

    x = ((a * 2) + (b * 3) + (c * 5)) / 10
    avg.append(x)

for k in avg:
    print(f"{k:.1f}")
