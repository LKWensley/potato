print('Игра "Угадай число"')

from random import randint

a = randint(1, 10)
i = 0

while i < 3:
    print('Осталось попыток: ',3-i)
    print('Введи число: ')
    try:
        b = int(input())
    except ValueError:
        print('Повтори ввод.')
    else:
        i += 1
        if a == b:
            print('Молодец! Ты угадал!')
            break
        elif a > b:
            print('Моё число больше.')
        else:
            print('Моё число меньше.')
            
print('Мое число: ',a)
