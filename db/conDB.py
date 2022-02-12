import sqlite3


class ConDB:
    # conn = sqlite3.connect('../db/db.db')
    connStr = 'db/db.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.connStr)
        self.conn.row_factory = sqlite3.Row

    def finalize(self):
        if self.conn:
            self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def __enter__(self):
        return self

    def getAllData(self):
        allEntry = self.conn.execute('SELECT * FROM posts').fetchall()
        return allEntry

    def getPost(self,post_id):
        allEntry = self.conn.execute('SELECT * FROM posts WHERE id =?',(post_id,)).fetchall()
        return allEntry

    def inserttodb(self,title,content):
        self.conn.execute('INSERT INTO posts (title,content) VALUES (?,?)',(title,content))
        self.conn.commit()

    def updatedb(self,title,content,id):
        self.conn.execute('UPDATE posts SET title = ?, content =? WHERE id =?', (title, content,id))
        self.conn.commit()

    def delete(self,id):
        self.conn.execute('DELETE FROM posts WHERE id = ?',(id,))
        self.conn.commit()

