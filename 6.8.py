# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

data = {
    'USA': ['NY', 'Vashington'],
    'Belarus': ['Minsk', 'Vitebsk']
}


def search_country(city: str) -> str:
    for i in data:
        for j in data[i]:
            if j == city:
                return i


print(search_country('NY'))
