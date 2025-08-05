import math
x = int(input())

j = 1

for i in range(x):
    print(f"{j*1} {pow(j,2)} {pow(j,3)}")
    print(f"{j*1} {pow(j,2)+1} {pow(j,3)+1}")
    j += 1
