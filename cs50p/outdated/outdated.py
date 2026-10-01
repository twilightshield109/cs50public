# format can be 9/8/1732 or September 8, 1732
monthslist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    date = input("Date: ").strip()
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        if month in monthslist:
            month = monthslist.index(month) + 1
    try:
        if int(month) > 12 or int(month) < 1 or int(day) > 31 or int(day) < 1:
            continue
        else:
            break
    except (ValueError, EOFError, NameError):
        continue

print(year + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")
