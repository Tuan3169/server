from ..extention import connect_database, close_database

def get_all_diemdanh():
    connect = connect_database()
    cursor = connect.execute("SELECT * FROM diemdanh")

    diemdanhs = [
        dict(id=row[0], img=row[1], date=row[2], user_id=row[3])
        for row in cursor.fetchall()
    ]

    close_database(connect)
    return diemdanhs

def get_diemdanh_user_id(user_id):
    connect = connect_database()
    cursor = connect.execute("SELECT * FROM diemdanh WHERE user_id = (?)", [user_id])
    
    diemdanhs = [
        dict(dict(id=row[0], img=row[1], date=row[2], user_id=row[3]))
        for row in cursor.fetchall()
    ]
    close_database(connect)
    return diemdanhs

def insert_diemdanh(diemdanh):
    connect = connect_database()
    connect.execute("""INSERT INTO DiemDanh (img, date, user_id) values (?,?,?)""",[diemdanh["img"], diemdanh["date"], diemdanh["user_id"]] )
    connect.commit()
    cursor = connect.execute("SELECT * FROM diemdanh WHERE user_id = (?)", [diemdanh["user_id"]])
    
    diemdanhs = [
        dict(dict(id=row[0], img=row[1], date=row[2], user_id=row[3]))
        for row in cursor.fetchall()
    ]
    close_database(connect)
    return diemdanhs

def get_diemdanh_id(id):
    connect = connect_database()
    cursor = connect.execute("SELECT * FROM diemdanh WHERE id = (?)", [id])
    
    diemdanhs = [
        dict(dict(id=row[0], img=row[1], date=row[2], user_id=row[3]))
        for row in cursor.fetchall()
    ]
    close_database(connect)
    return diemdanhs
