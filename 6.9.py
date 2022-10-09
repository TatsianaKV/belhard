#Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users = {
    1: {
        'name': 'Gleb',
        'email': 'gleb@info.com'
    },
    2: {
        'name': 'Masha',
        'email': ''
    },
    3: {
        'name': 'petya'
    }
}

def users_not_email(users: dict):
    for user in users.values():
        if not user.get('email'):
            print(user.get('name'))


users_not_email(users)

