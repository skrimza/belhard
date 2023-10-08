from pydantic import BaseModel, ValidationError
from typing import Optional, List
from csv import DictReader, DictWriter, reader, writer


class FromCsv(BaseModel):
    name: str
    age: int
    is_human: bool
    phone_number: str
    
    @classmethod
    def from_csv(cls, file):
        instances = []
        try:
            with open(file, 'r', encoding='utf-8') as input_file:
                csv_reader = DictReader(input_file)
                for line in csv_reader:
                    instance = cls(name=line['name'],
                                age=int(line['age']),
                                is_human=line['is_human'] == 'true',
                                phone_number=line['phone_number'])
                    instances.append(instance)
        except FileNotFoundError:
            print('Файл не найден')
        return instances
    
    
    def to_csv(self, file):
        try:
            with open(file, 'a', encoding='utf-8') as out:
                wiar = DictWriter(out, fieldnames=('name', 
                                                'age', 
                                                'is_human', 
                                                'phone_number'))
                wiar.writerow({'name': self.name, 
                            'age': self.age, 
                            'is_human': self.is_human, 
                            'phone_number': self.phone_number})
        except FileNotFoundError:
            print('Файл не найден')
        except ValidationError as e:
            print(f'ошибка в веденных данных: {e}')

csv_file = 'input.csv'
instances_list = FromCsv.from_csv(csv_file)
for inst in instances_list:
    print(inst)
    
csv_out = 'input.csv'
out_csv = FromCsv(name='Ilya', age=29, is_human=True, phone_number='+375291739013')
print(out_csv.to_csv(csv_out))
