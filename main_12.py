from psycopg2 import connect

conn = connect('postgresql://skrimza:60620IK@localhost:5432/belhard')

# with conn.cursor() as cur:
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS category(
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(64) NOT NULL UNIQUE
#         );
#     ''')
#     conn.commit()

# with conn.cursor() as cur:
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS post(
#             id SERIAL PRIMARY KEY,
#             title VARCHAR(128) NOT NULL,
#             description TEXT NOT NULL,
#             date_publish TIMESTAMP DEFAULT NOW(),
#             category_id INTEGER NOT NULL,
#             FOREIGN KEY (category_id) REFERENCES category(id)
#         );
#     ''')
#     conn.commit()
 
# with conn.cursor() as cur:
#     cur.executemany('''
#         INSERT INTO category (name)
#         VALUES (%s);
#     ''', (('finance', ), ('sport', )))
#     conn.commit()
#     cur.execute('''
#         INSERT INTO post (title, description, category_id)
#         VALUES (%s, %s, %s);      
#     ''', ('post 1', 'description', 1))
#     conn.commit()

with conn.cursor() as cur:
    cur.execute('''
        SELECT category.name, post.title FROM category
        JOIN post ON post.category_id = category.id
        ORDER BY category.name;
    ''')
    print(cur.fetchall())

