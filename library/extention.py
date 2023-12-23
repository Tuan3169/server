import sqlite3
from .config import DATABASE_URI

def create_database(DATABASE_URI):
    con = sqlite3.connect(DATABASE_URI)
    
    con.execute(""" CREATE TABLE IF NOT EXISTS account(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username CHAR NOT NULL,
                password CHAR NOT NULL
    )""")
    con.execute("""CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(100) NOT NULL,
    mssv NVARCHAR(10) NOT NULL,
    Avartar BLOB NULL,
    miss INTEGER NOT NULL,
    chucvi char not null,
    account_id integer not null,
    FOREIGN KEY(account_id) REFERENCES account(id)
    )""")
    con.execute("""CREATE TABLE IF NOT EXISTS DiemDanh (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    img BLOB NULL,
    date DATETIME NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(id)
    )""")

    con.close()

def connect_database():
    con = sqlite3.connect(DATABASE_URI)

    return con

def close_database(con):
    con.close()