a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

numbers = [a, b, c, d, e, f]

positive = sum(1 for num in numbers if num > 0)

s = 0
for j in numbers:
    if j > 0:
        s += j
    
avg = s / positive

print(f"{positive} valores positivos")
print(f"{avg:.1f}")