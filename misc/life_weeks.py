age = input("Enter ur age")

age_int = int(age)

years = 90 - age_int
days = years * 365
weeks = years * 52
months = years * 12

msg = (f"You have {days} days, {weeks} weeks and {months} months remaining")
print(msg)