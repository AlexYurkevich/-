import MySQLdb


db = MySQLdb.connect(
    host='localhost',
    user='newuser',
    passwd='123',
    db='horses_db'
)

c = db.cursor()


c.execute('SELECT * FROM my_app_horse;')

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()