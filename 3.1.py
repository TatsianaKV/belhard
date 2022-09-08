# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами

# 1 способ:

text = input('Введите хоть что-нибудь: ')
words = text.split()
text = '-'.join(words)
print(text)

# 2 cпособ

text = input('Введите что хотите: ')
print(text.replace(' ', '-'))
