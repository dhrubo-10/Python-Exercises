a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

numbers = [a, b, c, d, e]

even = sum(1 for num in numbers if num % 2 == 0)

print(f"{even} valores pares")