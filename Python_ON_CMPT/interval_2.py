a = int(input())

inp = 0
oup = 0

for i in range(a):
    x = int(input())

    if(10 <= x <= 20):
        inp += 1
    else:
        oup += 1
        
print(f"{inp} in")
print(f"{oup} out")