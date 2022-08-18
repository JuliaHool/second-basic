born_year = input('В каком году родился А.С. Пушкин? ')
while born_year != '1799':
    born_year = input('В каком году родился А.С. Пушкин? ')
if born_year == '1799':
    born_day = input('Когда день рождения А.С. Пушкина? ')
    while born_day != '6 июня':
        born_day = input('Когда день рождения А.С. Пушкина? ')
    if born_day == '6 июня':
        print('Верно')
