import pymysql.cursors

connection = pymysql.connect(host = '127.0.0.1',
                             user = 'root',
                             password = 'chatrapati@123',
                             db = 'college',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO 'users' ('email','password') VALUES (%s,%s)"
        cursor.execute(sql,('webmaster@python.org','very-secret'))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT 'id', 'password' FROM 'users' WHERE 'email'=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
