import string
import random


def examination():
    while True:
        i = input('Підкажи будь ласка яка довжина паролю повинна бути: ')
        if len(i):
            if i.isdigit():
                print(f'Довжина паролю: {i}')
                return int(i)
            else:
                print('Будь ласка, для вказування довжини використовуйте цифри! Спробуйте знову!')
                continue
        else:
            print('Пароль не може бути пустим! Спобуйте знову!')
            continue


def generate_password(length):
    my_string = string.ascii_letters + string.digits
    list = [char for char in my_string]
    password = ''.join(random.choice(list) for _ in range(length))
    return (password)


print(
'''
Привіт!\r
Ти в программі котра генерує пароль.
'''
)
while True:

    lenght = examination()
    password = generate_password(lenght)
    print (f'Ваш пароль виглядає так: {password}, його довжина : {lenght}')
    print('Бажаєте повторити?')
    inp_exit = input('Д,Y якщо бажаєте повторити.')
    if inp_exit.lower() not in ['y','д']:
        print('До нових зустріч!')
        break