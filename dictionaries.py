persons = {'Mark': '1-Jan-1970', 'John': '1-Jan-2000'}

print('I know the birthdays of: ')
for person in persons:
    print(f' - {person}')

person = input('Who\'s birthday you need?\n')

try:
    print(f'Birthday of {person} is {persons[person]}')
except KeyError:
    print(f'{person} not found in dictionary!')
