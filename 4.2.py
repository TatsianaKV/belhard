# создать программу, которая будет создавать словарь для подсчитывания количества
# вхождений каждой буквы в текст, введенной с клавиатуры:

text = input()
numbers_of_letters = {i: text.count(i) for i in text}
print(numbers_of_letters)