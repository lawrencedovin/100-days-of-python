age = input("What is your current age? > ")
age_in_weeks = int(age)*52

years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f'You are {age_in_weeks} weeks old.')
print(f'You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months remaining.')