# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
def numbers_list(numbers: list) -> list:
    c = 0
    for i in range(len(numbers)-1):
        b = numbers.pop(len(numbers)-1)
        numbers.insert(c, b)
        c += 1
    return numbers


print(numbers_list([1, 3, 6, 4]))
