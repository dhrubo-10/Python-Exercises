n = int(input())

c = 0
r = 0
s = 0
total = 0

avg1 = avg2 = avg3 = 0

for i in range(n):
    a,b = input().split()
    a = int(a)

    if 1 <= a <= 15:
        
        total += a
        if b == 'C':
            c += a
        
        elif b == 'R':
            r += a
        
        elif b == 'S':
            s += a
        
avg1 = (c / total) * 100
avg2 = (r / total) * 100
avg3 = (s / total) * 100
    
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {avg1:.2f} %")
print(f"Percentual de ratos: {avg2:.2f} %")
print(f"Percentual de sapos: {avg3:.2f} %")
        