wage = float(input("Hourly wage: "))
work = int(input("Hours worked: "))
day = input("Day of the week: ")

if (day == "Sunday"):
    print(f"Daily wages: {float((wage * 2) * work)} euros")
else:
    print(f"Daily wages: {float(wage * work)} euros")
