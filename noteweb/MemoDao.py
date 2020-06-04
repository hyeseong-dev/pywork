import sqlite3

class MemoDao:

    @staticmethod
    def connectCursor():
        conn = sqlite3.connect('note.db')
        cursor = conn.cursor()
        return cursor

    @staticmethod
    def selectMemos():
        cursor = MemoDao.connectCursor()
        cursor.execute('SELECT * FROM memo')
        memos = cursor.fetchall()
        cursor.close()
        return memos

    @staticmethod
    def selectMemo():
        pass

    @staticmethod
    def insertMemo(memo):
        conn = sqlite3.connect("note.db")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO memo(memo) values(?)', (memo,))
        conn.commit() 