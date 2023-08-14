import random

class Card:
    
    def __init__(self) -> None:
        self.__card_number = None
        self._discount = 5

    @property
    def _discount(self):
        return self.__discount

    @_discount.setter
    def _discount(self, value):
        if isinstance(value, int) and value >= 1:
            self.__discount = value
        else:
            raise ValueError('Ошибка проверки веденного значения')
        
    @property
    def card_number(self):
        return self.__card_number
    
    @card_number.setter
    def card_number(self, value):
        self.__card_number = value
        
class CardCreater(Card):
    card = []

    @classmethod
    def create(cls, quantity):
        for _ in range(quantity):
            new_card = Card()
            new_card.card_number = random.randint(1000, 9999)
            cls.card.append(new_card)

CardCreater.create(5)
for card in CardCreater.card:
    print(f'номер карты: {card.card_number}, дисконт: {card._discount}')

