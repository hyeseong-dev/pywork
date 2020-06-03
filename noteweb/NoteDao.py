import sqlite3

class NoteDao:  
    @staticmethod  
    def getCursor():
        db = sqlite3.connect('database.db')       
        cursor = db.cursor()
        return cursor

    @staticmethod  
    def selectMemos(): 
        cursor = NoteDao.getCursor().execute('SELECT * FROM note')        
        memos = cursor.fetchall()
        cursor.close()
        return memos

    @staticmethod  
    def selectMemo(idx): 
        cursor = NoteDao.getCursor().execute('SELECT memo FROM note WHERE idx=?;', (idx))        
        memo = cursor.fetchone()
        cursor.close()
        return memo        
