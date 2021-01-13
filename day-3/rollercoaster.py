print('Welcome to the Blizzard rollercoaster!')
height = int(input('What is your height in cm? '))

if height > 120:
    age = int(input('Welcome aboard what is your age? '))
    if age < 12:
        print('Child ticket is currently: $5')
        price = 5
    elif age < 18:
        print('Teen ticket is currently: $7')
        price = 7
    else:
        print('Adult ticket is currently: $12')
        price = 12

    want_photos = input('Do you want your photos? yes or no? ').lower()
    while want_photos != 'yes' or want_photos != 'no':
        if want_photos == 'yes':
            price += 3
            break
        elif want_photos == 'no':
            price = price
            break
        else:
            want_photos = input('Do you want your photos? yes or no? ').lower()

    print(f'Total bill is: ${price}')

else: 
    print('Too short, grow taller.')