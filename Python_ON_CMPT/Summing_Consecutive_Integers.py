sample = list(map(int,input().split()))

a = sample[0]
b = sample[-1]

total = [a]

for i in range(1,b):
    a += 1
    total.append(a)

result = sum(total)
print(result)