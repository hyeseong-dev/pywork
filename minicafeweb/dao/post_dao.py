from . import db

def select_posts():
    return db.select_all('SELECT * FROM post')

def select_post(no):
    return db.select_one('''
    SELECT * 
    FROM post 
    WHERE no=?
    ''', (no,))

