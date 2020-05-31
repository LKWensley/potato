import string
from random import choice

while 1:
    yn = str(input('Бросаем монетку? (д/н)\n'))
    yn = yn.lower()

    if yn not in ('д','н'):
        print('Повторите ввод.')
        
    elif yn in ('д'):
        coin = choice(['Eagle','Tails'])
        if coin == 'Eagle':
            print('Орёл')    
        elif coin == 'Tails':
            print('Решка')

    elif yn in ('н'):
        print('До свидания!')
        break

