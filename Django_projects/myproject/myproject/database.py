import pymysql

# Connection configuration
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Immamanu12!',
    database='project_database'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        print("Database version:", result[0])
finally:
    connection.close()


try:
    with connection.cursor() as cursor:
        cursor.execute("SHOW DATABASES;")
        for db in cursor.fetchall():
            print("Database:", db[0])
finally:
    connection.close()
