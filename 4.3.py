# Заполнить словарь, где ключами будут выступать числа от 0 до n,
# а  значениями вложенный словарь с ключами 'name'и 'e-mail',
# а значения для этих ключей будут браться с клавиатуры

key = int(input('Введите число: '))
dictionary = {i: {'name': input('Введите name: '), 'e-mail': input('Введите e-mail: ')} for i in range(key)}
print(dictionary)