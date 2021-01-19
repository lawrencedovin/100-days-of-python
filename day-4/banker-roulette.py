from random import randint

names = input('Input your names ie. Angela, Ben, Smith > ')
names = [name.strip() for name in names.split(',')]
person_to_pay = names[randint(0, (len(names)-1))]

print(f'{person_to_pay} is going to buy the meal today!')

