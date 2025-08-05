age = int(input())
sum = age
n = 1

while(True):
    age = int(input())
    if(age < 0):
        break
    else:
        sum += age
        n+=1
avg = sum / n
print(f"{avg:.2f}")
