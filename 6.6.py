#Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

def sorting_even_odd_numbers(numbers: list) -> list:
    even_numbers = []
    odd_numbers = []
    for i in numbers:
        if i % 2:
            odd_numbers.append(i)
        else:
            even_numbers.append(i)
    return[even_numbers, odd_numbers]


print(sorting_even_odd_numbers([1, 3, 4, 2, 5, 6]))
