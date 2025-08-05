a = int(input())

count = 0

if(a % 2 == 0):
        a += 1
else:
    pass

if(a > 0):
    
        
    while count < 6:
        if a % 2 != 0:
            print(a)
            a += 2
            count +=1
        else:
            a += 2
            count +=1
            print(a)