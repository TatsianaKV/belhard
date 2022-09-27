# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

# из десятичной в двоичную
def conversion_to_binary(number: int) -> str:
    x = ''
    while number >= 1:
        if number % 2:
            x = '1' + x
        else:
            x = '0' + x
        number = number // 2
    return x


print(conversion_to_binary(8))

# из двоичной в десятичную
def conversion_to_decimal(number: str) -> int:
    x = 0
    for i in number:
        x = x * 2 + int(i)
    return x


print(conversion_to_decimal('1000'))
