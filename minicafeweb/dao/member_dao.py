from . import db

def select_members():
    return db.select_all('SELECT * FROM member')

def select_member(no):
    return db.select_one('''
    SELECT * 
    FROM member 
    WHERE no=?
    ''', (no,))

def select_member_by_username_and_password(username, password):
    return db.select_one('''
    SELECT * 
    FROM member 
    WHERE username=? AND password=?
    ''', (username, password))

def insert_member(username, password, name):
    return db.insert('''
            INSERT INTO member (username, password, name) 
            VALUES (?, ?, ?)                    
            ''', (username, password, name))
