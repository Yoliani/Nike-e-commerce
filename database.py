import sqlite3



def sql_connection():
    con = sqlite3.connect('agenda.db')
    return con


def sql_insert(fullname, email, phone):
    strql = "INSERT INTO usuario(fullname, email, phone) values(?,?,?);"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strql, [fullname, email, phone])
    con.commit()
    con.close()

def sql_table(sentencia):
    strql = "SELECT * FROM usuario;"
    con = sql_connection() 
    cursor = con.cursor()
    cursor.execute(sentencia)
    data = cursor.fetchall()
    con.commit() 
    con.close() 
    return data
