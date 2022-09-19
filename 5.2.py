#   Создать калькулятор. Спрашивается число, действие и еще одно число

first_number = int(input('Первое число: '))
action = input('Введите действие: +  -  *  / ')
second_number = int(input('Второе число: '))

if action == "+":
    print('Результат:', first_number + second_number)
elif action == '-':
    print('Результат: ', first_number - second_number)
elif action == '*':
    print('Результат: ', first_number * second_number)
elif action == '/':
    print('Результат: ', first_number / second_number)
else:
    print('Проверьте действие !')




