from ..extention import connect_database, close_database

def get_all_user():
    connect = connect_database()
    cursor = connect.execute("SELECT * FROM user")

    users = [
        dict(id=row[0], name=row[1], mssv=row[2], avatar=row[3], miss=row[4], chucvi=row[5], account_id=row[6] )
        for row in cursor.fetchall()
    ]

    close_database(connect)

    return users

def get_user_account_id(account_id):
    connect = connect_database()
    cursor = connect.execute("""SELECT * FROM user WHERE account_id = (?)""", [account_id])

    user = [
        dict(id=row[0], name=row[1], mssv=row[2], avatar=row[3], miss=row[4], chucvi=row[5], account_id=row[6] )
        for row in cursor.fetchall()
    ]
    
    close_database(connect)
    return user

def get_user_id(id):
    connect = connect_database()
    cursor = connect.execute("""SELECT * FROM user WHERE id = (?)""", [id])

    user = [
        dict(id=row[0], name=row[1], mssv=row[2], avatar=row[3], miss=row[4], chucvi=row[5], account_id=row[6] )
        for row in cursor.fetchall()
    ]

    close_database(connect)
    return user

def update_avatar(id ,avatar):
    connect = connect_database()

    cursor = connect.execute("""SELECT * FROM user WHERE id = (?)""", [id])
    user = [
        dict(id=row[0], name=row[1], mssv=row[2], avatar=row[3], miss=row[4], chucvi=row[5], account_id=row[6] )
        for row in cursor.fetchall()
    ]
    
    if len(user) == 0:
        close_database(connect)
        return user
    else:
        connect.execute("""UPDATE user SET avatar = (?) WHERE id = (?)""", [avatar, id])
        connect.commit()
        cursor = connect.execute("""SELECT * FROM user WHERE id = (?)""", [id])

        user = [
            dict(id=row[0], name=row[1], mssv=row[2], avatar=row[3], miss=row[4], chucvi=row[5], account_id=row[6] )
            for row in cursor.fetchall()
        ]
    
        close_database(connect)
    return user