# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


def str_list(some_list: list) -> list:
    some_list = list(filter(lambda x: isinstance(x, str), some_list))
    return some_list


print(str_list([2, 4, 5, 'qw', 'sdsd', None, 4, True, 'wert']))
