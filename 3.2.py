# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3

first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
third_number = float(input('Введите третье число: '))
arithmetic_mean = (first_number + second_number + third_number) / 3
print('среднее арифметическое: ', round(arithmetic_mean, 3))
