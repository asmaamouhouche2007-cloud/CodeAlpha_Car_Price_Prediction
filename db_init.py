import sqlite3
def init_db():
    conn=sqlite3.connect('predictions.db')
    cursor=conn.cursor()
    with open('schema.sql') as f :
        cursor.executescript(f.read())
    conn.commit()
    conn.close()
if __name__=='__main__':
    init_db()

