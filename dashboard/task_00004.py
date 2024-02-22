"""
Нам нужна функция, которая может преобразовать число (целое) в строку.
Какие способы достижения этой цели вы знаете?
"""
def number_to_string(num):
    if type(num) == int:
        return str(num)

    else:
        print('Not int')

number_to_string(123)
number_to_string(999)
number_to_string(-999)
