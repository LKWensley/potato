from math import sqrt
print('Решалка квадратных уравнений. Дискриминант.')

while 1:
    try:
        a = int(input('Введите число A:\n'))
    except ValueError:
        print('Повторите ввод.')
    else:
        if a < 0:
            print('Число меньше нуля. Повторите ввод.')
        elif a == 0:
            print('Число равно нулю. Повторите ввод.')
        else:
            break

while a>0:
    try:
        b = int(input('Введите число B:\n'))
    except ValueError:
        print('Повторите ввод.')
    else:
        break

while 1:
    try:
        c = int(input('Введите число C:\n'))
    except ValueError:
        print('Повторите ввод.')
    else:
        break


print('Дискриминант равен:')
D = (b ** 2) - 4*a*c
print('D = ({0})^2 - 4*{1}*{2} = {3}.'.format(b,a,c,D))

if D < 0:
    print('Ответ: Корней нет.')
else:
    x1 = (-b + sqrt(D))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)
    print('x1 = ({0} + {1})/(2*{2}) = {3}'.format(-b,sqrt(D),a,x1))
    print('x2 = ({0} - {1})/(2*{2}) = {3}'.format(-b,sqrt(D),a,x2))
    print('Ответ: x1 = {0}, x2 = {1}.'.format(x1,x2))

    
