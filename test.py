import pymysql

def get_maintag(filename,table):

    for line in open(filename):
        maintag_data = line.strip().split(',')
        insertSql = 'insert into '


connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='benf',
    passwd='',
)

cursor = connect.cursor()
createDBsql = 'create database if not exist %s'
cursor.execute(sql)
db = cursor.fetchall()
print(db)
connect.commit()
connect.close()
get_maintag("C:\\Users\\benfzhang\Desktop\\1.txt")