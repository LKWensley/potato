while True:
    pol = input('Введите свой пол:\n')
    if pol in ('м', 'М'):
        print('Мне нравятся мальчики')
        break
    elif pol in ('д', 'Д'):
        print('Мне нравятся девочки')
        break
    else:
        print('Повторите ввод')
        
    
