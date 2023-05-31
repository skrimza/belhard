# * a dictionary of dictionaries is given, the key of external dictionary is id user, 
# value is dictionary with data users(name, surname, phone, email. need to output name, 
# whose email is not specify or empty string


def sorted_account():
    dict_account = {
        'id1': {
            'name': 'Vasya',
            'surname': 'Pupkin',
            'phone': '+375291739015',
            'mail': 'vasya@mail.ru'
        }, 'id2': {
            'name': 'Kasya',
            'surname': 'Sopkin',
            'phone': '+375336062073',
        }, 'id3': {
            'name': 'Vitya',
            'surname': 'Lapkin',
            'phone': '+375447266767',
            'mail': ''
        }, 'id4': {
            'name': 'Pilya',
            'surname': 'Shapkin',
            'phone': '+375447265689',
            'mail': 'kosulya@gmail.com'
        }
    }
    return [user.get('name') for user in dict_account.values() if not user.get('mail')]

res = sorted_account()
print(res)

