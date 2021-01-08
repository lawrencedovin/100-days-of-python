print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
percentage_tip = float(input('What percentage tip would you like to give? 10, 12, or 15? ')) / 100
people = int(input('How many people to split the bill? '))
total_per_person = round(((total_bill*percentage_tip) + total_bill)/people, 2)
print(f'Each person should pay: ${total_per_person}')