from sys import exit

while True:
    t = input('Сегодня у нас в продаже новые выпуски газет и журналов.\nЧто желаете купить: газету или журнал? (г/ж)\n')
    
    if t not in ('г','Г','ж','Ж'):
        print('Повторите ввод.')
    else:
        for t in ('г','Г','ж','Ж'):
            try:
                n = int(input('Сколько возьмёте?\n'))
            except ValueError:
                print('Повторите ввод.')
            else:
                for t in ('ж','Ж','г','Г'):
                    if t in ('ж','Ж'):
                        st = n*20
                    elif t in ('г','Г'):
                        st = n*10
                    print('С вас {} рублей. Платите.'.format(st))
                    while True:
                        try:
                            d = int(input())
                        except ValueError:
                            print('Повторите ввод.')
                        else:
                            break
                    if d<st:
                        while True:
                            print('Не хватает средств. Доплатите {} рублей.'.format(st-d))
                            try:
                                d1 = int(input())
                            except ValueError:
                                print('Повторите ввод.')
                            else:
                                d = d+d1
                                if d >= st:
                                    print('Получите сдачу {} рублей. Спасибо за покупку'.format(d-st))
                                    exit(0)
                    else:
                        print('Получите сдачу {} рублей. Спасибо за покупку'.format(d-st))
                        exit(0)
