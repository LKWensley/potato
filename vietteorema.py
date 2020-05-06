from random import randint

print('Решалка квадратных уравнений. Теорема Виета.')

while 1:
    try:
        p = int(input('Введите число P:'))
    except ValueError:
        print('Повторите ввод.')
    else:
        break

while 1:
    try:
        q = int(input('Введите число Q:'))
    except ValueError:
        print('Повторите ввод.')
    else:
        break

print('x^2 + ',p,'x + ',q,' = 0')

print('x1 + x2 =',-p)
print('x1 * x2 =',q)

while True:
    x1 = randint(-100,100)
    x2 = randint(-100,100)
    if x1+x2 == -p and x1*x2 == q:
        print('Ответ: x1= {0}, x2= {1}.'.format(x1, x2) )
        break
    else:
        k =+ 1
        if k > 100:
            print('Вариантов больше нет. Возможно, через теорему решить невозможно.')
            break
        
