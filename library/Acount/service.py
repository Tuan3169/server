from ..extention import connect_database, close_database

def get_all_account():
    connect = connect_database()

    cursor = connect.execute("SELECT * FROM account")
    accounts = [
        dict(id=row[0], username=row[1], password=row[2])
        for row in cursor.fetchall()
    ]

    close_database(connect)

    return accounts

def check_account(account_name, password):
    connect = connect_database()
    
    cursor = connect.execute("""SELECT * FROM account WHERE username = (?)""", [account_name])
    connect.commit()

    account = [
        dict(id=row[0], username=row[1], password=row[2])
        for row in cursor.fetchall()
    ]
    close_database(connect)
    return account

def create_account(user_id, account_inf, user_inf):
    connect = connect_database()
    cursor = connect.execute("""SELECT chucvi FROM user WHERE id = (?)""", [user_id])

    chucvi = cursor.fetchone()

    if(chucvi=="admin"):
        cursor = connect.execute("""SELECT id FROM account WHERE username=(?)""", [account_inf["username"]])
        result = cursor.fetchall()
        if result.__len__ != 0:
            return "username used!", 400
        
        connect.execute("""INSERT INTO account (username, password) values (?,?)""", [account_inf["username"], account_inf["password"]])
        connect.commit()
        cursor = connect.execute("""SELECT id FROM account WHERE username = (?)""", [account_inf["username"]])
        account_id = cursor.fetchone()[0]
        connect.execute("""INSERT INTO user(name, mssv, avatar, miss, chucvi, account_id, ngaysinh) values (?,?,?,?,?,?,?)""",
                        [user_inf["name"], user_inf["mssv"], user_inf["avatar"], user_inf["miss"], user_inf["chucvi"], account_id,
                         user_inf["ngaysinh"]])
        connect.commit()

        return "success!", 200
    else:
        return "you isn't admin!", 400