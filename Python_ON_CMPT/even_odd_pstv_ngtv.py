a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

numbers = [a, b, c, d, e]

even = sum(1 for num in numbers if num % 2 == 0)

odd = sum(1 for num in numbers if num % 2 != 0)

positive = sum(1 for num in numbers if num > 0)

negative = sum(1 for num in numbers if num < 0)

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")