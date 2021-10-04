# Написать программу, которая запрашивает у
# пользователя данные такие как:
# Имя персонажа, его силу атаки(макс 100)
# и его ловкость(макс 100),
# затем сохраняет данные в файл db.json и
# сохраняет до тех пор,
# пока пользоваетль не решит сам остановиться.
# Также есть функция,
# которая в рандомном порядке вытаскивает 2х
# игроков(использовать библиотеку random)
# и между ними идет бой, победит тот у кого больше
# силы и ловкости, если у первого игрока силы больше,
# но ловкости меньше мин на 10 пунктов, то побеждает
# игрок у которого больше ловкости,
# после боя программа спрашивает у пользователя хочет
# ли он устроить еще один
# бой либо добавить еще одного игрока или может вообще
# выйти из игры.
# Вывод программы должен сопровождаться сообщениями
# типа: Данные сохранены!, Бой начался!,
# Победил игрок: Игрок1! и тд.

import json
import random

data = []

def file():
    global data
    with open('dp.json', 'r+') as f:
        data = json.loads(f.read())
        

def info():
    global data
    file()
    print(data)


def write_data():
    global data
    nameoh = input('введите имя персонажа: ')
    strengthoh = input('введите силу персонажа(max 100): ')
    agilityoh = input('введите ловкость персонажа(max 100): ')
    new_data = {
        "name": nameoh,
        "strengh": strengthoh,
        "agility": agilityoh
    }
    
    with open('dp.json', 'r+') as f:
        data = json.loads(f.read())
        data.append(new_data)
        print(data)
    
    with open('dp.json', 'w') as h:
        json.dump(data, h)

    answ = input('данные сохранены, добавить еще? данные/бой/отмена/инфа: ')
    if answ == 'данные':
        write_data()
    elif answ == 'бой':
        battle()
    elif answ == 'инфа':
        info()
    elif answ == 'отмена':
        pass

def battle():
    global data
    file()
    a = random.sample(data, 2)
    print(a)
    b = a[0]
    c = a[1]
    b0 = b['name']
    c0 = c['name']
    b1 = b['strengh']
    c1 = c['strengh']
    b2 = b['agility']
    c2 = c['agility']
    if b1 < c1 and c2 > b2:
        print('c')
    elif c1 < b1 and b2 > c2:
        print('b')
    fg = input('хотите повторить? да/нет: ')
    if fg == 'да':
        manager()

def manager():
    answ = input('вы хотите добавить данные или начать бой? данные/бой/отмена/инфа: ')
    if answ == 'данные':
        write_data()
    elif answ == 'бой':
        battle()
    elif answ == 'инфа':
        info()
    elif answ == 'отмена':
        pass
    else:
        print('вы ввели некоректные данные!')

manager()

