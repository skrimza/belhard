from sqlalchemy import (Column, 
                        TIMESTAMP, 
                        ForeignKey, 
                        INTEGER, 
                        VARCHAR, 
                        create_engine)
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker
from typing import Optional, Union
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class Base(DeclarativeBase):
    # базовая модель для создания таблиц данных
    id = Column(INTEGER, primary_key=True)
    engine = create_engine('postgresql://skrimza:60620IK@127.0.0.1:5432/belhard')
    session = sessionmaker(bind=engine)
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        # Генерация названий таблиц исходя из названий классов
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

class Personal(Base):
    # создание таблицы personal для записи данных персонала
    name = Column(VARCHAR(24), nullable=False, index=True)
    email = Column(VARCHAR(64), unique=True, nullable=False, index=True)
    status = Column(INTEGER, nullable=False)
    date_publish = Column(TIMESTAMP, default=datetime.now())

    
class Guest(Base):
    # создание таблицы Guest для записи данных гостя
    name = Column(VARCHAR(24), nullable=False, index=True)
    email = Column(VARCHAR(64), unique=True, nullable=False)
    phone_number = Column(VARCHAR(16), unique=True, nullable=True)
    country = Column(VARCHAR(24), nullable=True)
    date_publish = Column(TIMESTAMP, default=datetime.now())
    personal_id = Column(INTEGER, ForeignKey('personal.id', ondelete='CASCADE'), nullable=False)

class MyCat:
    # Данный класс проводит проверку 
    # введенного номера таблицы пользователем
    
    @classmethod
    def choise_db(cls, choise):
        while int(choise) not in [1, 2]:
            choise = input('Неправильно, еще раз (1, 2): ')
        return int(choise)


class FirstScheme(BaseModel):
    # первая схема базовой модели для 
    # валидации данных к таблице Personal
    name: str = Field(..., min_length=4, max_length=16)
    email: EmailStr = Field(...)
    status: int = Field(default=0)
    
    class Config:
        from_attributes = True
    
class SecondScheme(BaseModel):
    # вторая схема базовой модели для 
    # валидации данных к таблице Personal
    name: str = Field(..., min_length=4, max_length=16)
    email: EmailStr = Field(...)
    phone_number: Optional[str]
    country: str = Field(..., max_length=36)
    personal_id: int
    
    class Config:
        from_attributes = True

def menu(table: int):
    while True:
        print ("Выберете действие:")
        print ("1. Ввести данные")
        print ("2. Получить все данные")
        print ("3. Вернуться к списку таблиц")
        choise = input("Введите Ваш выбор (1,2,3): ")
        if choise == '1':
            foo_start(table)
        elif choise == '2':
            retrieve_data(table)
        elif choise == '3':
            return
        else:
            print('Неправильный выбор, пожалуйста, выберете 1,2 или 3.')
            
def foo_start(res_my_cat):
    # функция для проверки выбора таблицы данных 
    # пользователя
    while True:
        try:
            if res_my_cat == 1:
                with Personal.session() as session:
                    result = Personal(**FirstScheme(name=input('Введите имя: '), 
                                        email=input('Введите Email: '), 
                                        status=int(input('Введите персональный статус: '))).model_dump())
                    session.add(result)
                    session.commit()
                    session.refresh(result)
            else:
                with Guest.session() as session:
                    result = Guest(**SecondScheme(name=input('Введите имя: '), 
                                        email=input('Введите Email: '), 
                                        phone_number=input('Введите номер телефона: '),
                                        country=input('Введите Вашу страну: '),
                                        personal_id=int(input('Введите ID personal: '))).model_dump())
                    session.add(result)
                    session.commit()
                    session.refresh(result)
            print('Данные успешно внесены')
            sasha = result.__dict__
            del sasha['_sa_instance_state']
            print(sasha)
            break
        except Exception as e:
            print('Ошибка при вводе данных:', str(e))
            retry = input('Хотите повторно ввести данные? (да/нет): ')
            if retry.lower() != 'да':
                break

def retrieve_data(res_my_cat):
    if res_my_cat == 1:
        with Personal.session() as session:
            data = session.query(Personal.id, Personal.name, Personal.status, Personal.email).all()
            for item in data:
                print([*item])
    else:
        with Guest.session() as session:
            data = session.query(Guest.id, Guest.name, Guest.email, Guest.phone_number, Guest.country).all()
            for item in data:
                print([*item])


while True:
    choise = input('таблица данных(1, 2) или "q" для выхода из программы: ').strip()
    if choise == '1':
        menu(1)
    elif choise == '2':
        menu(2)