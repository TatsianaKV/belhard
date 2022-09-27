# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


def list_shift(numbers: list, n=int(input('На сколько смещать: '))) -> list:
    for i in range(abs(n)):
        if n > 0:
            b = numbers.pop(len(numbers) - 1)
            numbers.insert(0, b)
        else:
            b = numbers.pop(0)
            numbers.append(b)
    return numbers


print(list_shift(numbers=[1, 2, 3, 4, 5]))
