year = int(input('Which year do you want to check? '))

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return 'Leap year.' if year % 400 == 0 else 'Not Leap year.'
        return('Leap year.')
    else:
        return('Not Leap year.')

print(leap_year(year))

