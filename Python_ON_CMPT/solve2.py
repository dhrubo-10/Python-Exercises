start_day = int(input().split()[-1])
start_time = input()
end_day = int(input().split()[-1])
end_time = input()

s_hour, s_min, s_sec = map(int, start_time.split(' : '))
e_hour, e_min, e_sec = map(int, end_time.split(' : '))

t1 = (start_day * 24 * 60 * 60) + (s_hour * 60 * 60) + (s_min * 60) + s_sec
t2 = (end_day * 24 * 60 * 60) + (e_hour * 60 * 60) + (e_min * 60) + e_sec

day = hour = minute = second = 0

for i in range(t1, t2):
    second += 1
    
    if second == 60:
        minute += 1
        second = 0
        
        if minute == 60:
            hour += 1
            minute = 0
            
            if hour == 24:
                day += 1
                hour = 0

print(f'''{day} dia(s)
{hour} hora(s)
{minute} minuto(s)
{second} segundo(s)''')
