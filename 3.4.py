# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

first_number = input("Введите первое число: ")
second_number = input('Введите второе число: ')
third_number = input('Введите третье число: ')
numbers = first_number + second_number + third_number
negative_number = numbers.count('-')
pozitive_number = 3 - negative_number
print('отрицательных чисел: ', negative_number)
print('положительных чисел: ', pozitive_number)

