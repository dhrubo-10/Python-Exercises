a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

numbers = [a, b, c, d, e, f]

positive = sum(1 for num in numbers if num > 0)
print(f"{positive} valores positivos")