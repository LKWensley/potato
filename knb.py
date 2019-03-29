print('Камень, ножницы, бумага')
from random import choice
import string

while 1:
    qstn = input('Будешь играть? (д/н)\n')
    
    if qstn not in ('д','Д','н','Н'):
        print('Повторите ввод.')
        
    elif qstn in ('н','Н'):
        print('До свидания!')
        break
    
    elif qstn in ('д','Д'):
        
        while True:
            a = input('Что выберешь:\nкамень (к), ножницы (н) или бумагу (б)?\n')
            b = choice('кнб')
            if a not in ('к','н','б'):
                print('Повторите ввод.')
            else:
                
                if a == b:
                    print('Ничья.')
                    
                elif a == ('б') and b == ('н'):
                    print('Я выбрал ножницы.')
                    print('Ножницы режут бумагу.')
                    print('Я победил.')
                    break
                
                elif a == ('к') and b == ('н'):
                    print('Я выбрал ножницы.')
                    print('Камень ломает ножницы.')
                    print('Ты победил.')
                    break
                
                elif a == ('к') and b == ('б'):
                    print('Я выбрал бумагу.')
                    print('Бумага накрыла камень.')
                    print('Я победил.')
                    break
                
                elif a == ('н') and b == ('б'):
                    print('Я выбрал бумагу.')
                    print('Ножницы режут бумагу.')
                    print('Ты победил.')
                    break
                
                elif a == ('н') and b == ('к'):
                    print('Я выбрал камень.')
                    print('Камень ломает ножницы.')
                    print('Я победил.')
                    break
                
                elif a == ('б') and b == ('к'):
                    print('Я выбрал камень.')
                    print('Бумага накрыла камень.')
                    print('Ты победил.')
                    break


