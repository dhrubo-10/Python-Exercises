months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    user_date = input("Date: ")
    try:
        month, day, year = user_date.split("/")
        month = month.replace(" ", "")
        year = year.replace(" ", "")
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except:
        try:
            prvsm, prvsd, year = user_date.split(" ")
            for m in range(len(months)):
                if prvsm == months[m]:
                    month = m + 1
            if not prvsd.endswith(","):
                continue
            else:
                day = prvsd.replace(",", "")
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
