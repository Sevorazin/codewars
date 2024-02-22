def is_prime(number):
    """
    Перевіряє, чи є задане число простим.

    :param number: Число для перевірки
    :return: True, якщо число просте, інакше False
    """
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Перевіряємо дільники від 3 до квадратного кореня числа
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Приклад використання
while True:
    num_to_check = int(input())
    if is_prime(num_to_check):
        print(f"{num_to_check} є простим числом.")
    else:
        print(f"{num_to_check} не є простим числом.")
    inp_ex = input('Y\Д')
    if inp_ex.lower() in ['y','д']:
        break