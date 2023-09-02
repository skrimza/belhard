from sqlite3 import *
from pydantic import BaseModel, Field
from csv import DictReader, DictWriter

conn = connect('database.sqlite3')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) NOT NULL UNIQUE,
        is_published INTEGER
    );       
''')
conn.commit()

class PySchem(BaseModel):
    name: str = Field(..., min_length=3, max_length=32)
    is_published: bool = Field(...)
    
    @classmethod
    def from_csv(cls, file):
        instance = []
        with open(file, 'r', encoding='utf-8') as file:
            read_text = DictReader(file)
            for line in read_text:
                instance.append(cls(name=line['name'],
                                    is_published=line['is_published']))
        return instance
    
    @staticmethod
    def export_csv(instance):
        with connect('database.sqlite3') as connection:
            curs = connection.cursor()
            data = [(i.name, int(i.is_published)) for i in instance]
            curs.execute('''
                INSERT INTO category (NAME, IS_PUBLISHED)
                VALUES (?, ?)                   
            ''', data)
            connection.commit()
    
    @staticmethod
    def update_csv(new_name, new_published):
        with connect('database.sqlite3') as connection:
            curs = connection.cursor()
            curs.execute('''
                INSERT INTO category (NAME, IS_PUBLISHED)
                VALUES (?, ?)                   
            ''', (new_name, new_published))
            connection.commit()
            
    @staticmethod
    def delete_from_db():
        with connect('database.sqlite3') as connection:
            curs = connection.cursor()
            sqlite_del = '''
                DELETE FROM category WHERE IS_PUBLISHED = ?;     
            '''
            
            curs.execute(sqlite_del, (False, ))
            connection.commit()
    
    @classmethod
    def into_csv(cls, dict_read):
        data = dict_read
        with (connect('database.sqlite3') as connection):
            
            
            cursor = connection.cursor()
            from_db = '''SELECT NAME, IS_PUBLISHED FROM category'''
            cursor.execute(from_db)
            with open('input.csv', 'a', encoding='utf-8') as output:
                rewrite_text = DictWriter(output, fieldnames=('name', 'is_published'))
                data_b = cursor.fetchall()
                for i in data_b:
                    if i[0] not in [j.name for j in data]:
                        rewrite_text.writerow({'name': i[0],
                                                'is_published': bool(i[1])})

csv_file = 'input.csv'
scheme = PySchem.from_csv(csv_file)

# from_csv = PySchem.export_csv(scheme)
# print(from_csv)
# update_csv = PySchem.update_csv('Sandra', True)
# del_db = PySchem.delete_from_db()
# print(del_db)

from_db = PySchem.into_csv(scheme)
print(from_db)