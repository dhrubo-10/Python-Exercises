start_day = int(input().split()[-1])
start_time = input()
end_day = int(input().split()[-1])
end_time = input()

s_hour, s_min, s_sec = map(int, start_time.split(' : '))
e_hour, e_min, e_sec = map(int, end_time.split(' : '))

t1 = (start_day * 24 * 60 * 60) + (s_hour * 60 * 60) + (s_min * 60) + s_sec
t2 = (end_day * 24 * 60 * 60) + (e_hour * 60 * 60) + (e_min * 60) + e_sec

total_seconds = t2 - t1

day = total_seconds // (24 * 60 * 60)
total_seconds %= 24 * 60 * 60

hour = total_seconds // (60 * 60)
total_seconds %= 60 * 60

minute = total_seconds // 60
total_seconds %= 60

second = total_seconds

print(f"The event lasted for {day} days, {hour} hours, {minute} minutes, and {second} seconds.")
