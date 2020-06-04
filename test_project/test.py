import sqlite3

print ('hello world')

# DB 연결
conn = sqlite3.connect('my.db')
cursor = conn.cursor()

# INSERT 문
memo = '1234'
cursor.execute('INSERT INTO memo(memo) VALUES(?)', (memo,)) 
conn.commit()

# SELECT 문 - 한개
cursor.execute('SELECT * FROM memo WHERE no=2')
memo = cursor.fetchone()
print('memo(%s, %s)' % (memo[0], memo[1]))

# SELECT 문 - 리스트
cursor.execute('SELECT * FROM memo')
memos = cursor.fetchall()
for memo in memos:
    print('memo(%s, %s)' % (memo[0], memo[1]))
