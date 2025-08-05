value = 0
position = 0

for i in range(1, 101):
    n = int(input())

    if value < n:
        value = n
        position = i

print(value)
print(position)