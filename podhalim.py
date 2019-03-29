while True:
    pol = input('Введите свой пол:\n')
    if pol not in ('м', 'М'):
        if pol not in ('д', 'Д'):
            print('Повторите ввод.')
        else:
            print('Мне нравятся девочки')
            break
    else:
        print('Мне нравятся мальчики')
        break
    
