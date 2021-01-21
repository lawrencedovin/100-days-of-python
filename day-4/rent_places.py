cities = ['Rockville', 'Bethesda', 'Gaithersburg', 'Germantown', 'Olney',
            'Potomac', 'Takoma Park', 'Monthgomery Village', 'Wheaton', 'Clarksburg',
            'White Oak', 'Kensington', 'Burtonsville', 'North Potomac', 'North Bethesda',
            'Poolesville', 'Aspen Hill', 'Boyds', 'Darnestown', 'Damascus',
            'Brookeville', 'Colesville', 'Garrett Park', 'Laytonsville', 'Chevy Chase',
            'Washington Grove', 'Cabin John', 'Glen Echo', 'Fairland', 'Barnesville',
            'Leisure World', 'Cloverly', 'Dickerson', 'Kemp Mill', 'Travilah',
            'Chevy Chase View', 'Ashton-Sandy Spring', 'Friendship Village', 'North Kensington',
            'Kensingston', 'South Kensington', 'Redland', 'Brookmont', 'Somerset',
            'Silver Spring']

sorted_cities = sorted(city.lower() for city in cities)

answer = int(input('Alphabetical order type 1 check by town type 2 > '))

if answer == 1:
    for index, city in enumerate(sorted_cities):
        print(f'{index + 1}. {city.title()}')
if answer == 2:
    check_city = input('What city do you want to check if it exists > ')
    print(f'{check_city.title()} is in Montgomery County') if check_city.lower() in sorted_cities else print(f'{check_city.title()} is NOT in Montgomery County')