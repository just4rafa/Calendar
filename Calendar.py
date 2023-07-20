import calendar

year = int(input("Enter the Year : "))
month = int(input("Enter the Month : "))

calendar.setfirstweekday(calendar.SUNDAY)
mycal = calendar.month(year, month)

print()
print(mycal)
