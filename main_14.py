owner_dict = {
    'name': 'Ilya',
    'age': 29,
    'languages': ['en', 'ru', 'by'],
}

print(key for key in owner_dict.keys() if owner_dict[key].isdigit())
    