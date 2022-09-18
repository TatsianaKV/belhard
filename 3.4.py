# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

first_number = -5
second_number = -3
third_number = 0
numbers = str(first_number) + str(second_number) + str(third_number)
print(numbers)
negative_number = numbers.count('-')
pozitive_number = 3 - negative_number
print('отрицательных чисел: ', negative_number)
print('положительных чисел: ', pozitive_number)

a = [3, 0, -3, 0]
poz = sum(i>0 for i in a)
neg = sum(i<0 for i in a)
print(poz)
print(neg)




