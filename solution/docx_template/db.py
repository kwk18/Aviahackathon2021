import sqlite3
from sqlite3 import Error
import logging


logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)


def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        logging.info("SQL connected")


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE passengers2(id integer PRIMARY KEY, first_name text, last_name text, pass_number text, pass_info text, reg_address text, tel text)")
    con.commit()


def sql_insert(con, entites):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO passengers2(id, first_name, last_name, pass_number, pass_info, reg_address, tel) VALUES(?, ?, ?, ?, ?, ?, ?)', entites)
    con.commit()


def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM passengers')
    rows = cursorObj.fetchall()
    return rows


def sql_find_person(con, tel_number):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, first_name, last_name, pass_number, pass_info, reg_address FROM passengers2 WHERE tel=?', (tel_number,))
    # logging.log(first_name + " " + last_name + " found in DB")
    return cursorObj.fetchall()


con = sql_connection()
# sql_table(con)


if __name__ == "__main__":
    # con = sql_connection()
    sql_table(con)
    entites = (1, "John", "Smith", "6700 4234523", "МО УФМС ПО ГОРОДУ City_name", "ул. Пушкина, дом Колотушкина", "+71234567890")
    sql_insert(con, entites)

    sql_fetch(con)



