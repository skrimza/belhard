from sqlalchemy import (Column, 
                        TIMESTAMP, 
                        ForeignKey, 
                        INTEGER, 
                        BOOLEAN, 
                        VARCHAR, 
                        TEXT,
                        create_engine,
                        DateTime,
                        DATE,
                        DATETIME)
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker
from typing import Optional, Union
from pydantic import BaseModel, Field, EmailStr

# class Base(DeclarativeBase):
#    id = Column(int, primary_key=True)
    
#     @declared_attr
#     def __tablename__(cls):
#         return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

# class Personal(Base):
#     name = Column(VARCHAR(24), nullable=False, index=True)
#     email = Column(VARCHAR(64), unique=True, nullable=False, index=True)
#     status = Column(INTEGER, nullable=False)
#     date_publish = Column(TIMESTAMP, default=DateTime.now())

    
# class Guest(Base):
#     name = Column(VARCHAR(24), nullable=False, index=True)
#     email = Column(VARCHAR(64), unique=True, nullable=False)
#     phone_number = Column(VARCHAR(16), unique=True, nullable=True)
#     country = Column(VARCHAR(24), nullable=True)
#     date_publish = Column(TIMESTAMP, default=DateTime.now())



class MyCat:
    
    @classmethod
    def choise_db(cls, choise):
        while int(choise) not in [1, 2]:
            choise = input('Неправильно, еще раз (1, 2): ')
        return int(choise)


class FirstScheme(BaseModel):
    name: str = Field(..., min_length=4, max_length=16)
    email: EmailStr = Field(...)
    status: int = Field(le=5)
    
    class Config:
        orm_mode = True
    
class SecondScheme(BaseModel):
    name: str = Field(..., min_length=4, max_length=16)
    email: EmailStr = Field(...)
    phone_number: Optional[str]
    country: str = Field(..., max_length=36)
    
    class Config:
        orm_mode = True

def foo_start(res_my_cat):
    if res_my_cat == 1:
        result = FirstScheme(name=input('Введите имя: '), 
                            email=input('Введите Email:'), 
                            status=int(input('Введите Ваш персональный статус: ')))
        print(result.model_dump())
    else:
        result = SecondScheme(name=input('Введите имя: '), 
                            email=input('Введите Email:'), 
                            phone_number=input('Введите номер телефона: '),
                            country=input('Введите Вашу страну: '))
        print(result.model_dump())

choise = input('таблица данных(1, 2): ')
res_my_cat = MyCat().choise_db(choise)
foo_start(res_my_cat)
