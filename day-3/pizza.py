print('MAMA MIA PIZZARIA')
size = input('What a size u want your pizzaria? L, M, S: ').upper()
add_pepperoni = input('Do you want pepperoni? Y or N: ').upper()
extra_cheese = input('Do you want extra cheese? Y or N: ').upper()

if size == 'L':
    price = 25
if size == 'M':
    price = 20
if size == 'S':
    price = 15

if add_pepperoni == 'Y':
    if size == 'M' or size == 'L':
        price += 3
    else:
         price += 2

if extra_cheese == 'Y':
    price += 1

print(f'Your final bill is: ${price}')
