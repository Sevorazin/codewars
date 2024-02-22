print('Завдання №1')
print('Напишіть программу калькулятор,'
      ' котра приймає 2 числа і виконує основні математичні операції:'
      ' додавання,'
      ' віднімання,'
      ' множення,'
      ' ділення.'
      )
print('-'*135)
while True:
    while True:
        first_inp = input('Введіть будь ласка 1-ше число: ')
        if first_inp.isdigit():
            first_int = int(first_inp)
            break
        else:
            print('З вашим числом щось не так,'
                  'спробуйте ще раз!')
            continue

    while True:
        second_inp = input('Введіть будь ласка 2-ге число: ')
        if second_inp.isdigit():
            second_int = int(second_inp)
            break
        else:
            print('З вашим числом щось не так,'
                  'спробуйте ще раз!')
            continue


    print(f'\nСумма обох чисел: {first_int + second_int}')
    print(f'Різниця обох чисел: {first_int - second_int}')
    print(f'Добуток обох чисел: {first_int * second_int}')
    print(f'Частка обох чисел: {first_int / second_int}')

    exit_inp = input('Якщо хочете вийти : Y,Д'
                     '\nЯкщо повторити то залиште поле пустим.'
                     '\nЩо бажаете: ')
    if exit_inp.lower() in ['y', 'д']:
        print('До зустрічі!')
        break
    else:
        continue