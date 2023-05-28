# * the dictionary is given, key is name of country, value is a list of cities
# in input arrived city, need to sayd which country he is from

def find_country(city_message):
    country_city = {
        'Russia': [
            'Moscow',
            'Sanct-Petersburg',
            'Vladivostok'
        ], 'USA': [
            'Texas',
            'New-york',
            'Washington'
        ], 'Germany': [
            'Hamburg',
            'Berlin',
            'Keln'
        ]
    }
    for country, city in country_city.items():
        for i in city:
            if i == city_message.capitalize():
                print(country)

find_country(input('input city: '))


