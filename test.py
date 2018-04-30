# -*- coding:utf-8 -*-
import pymysql
'''
	pymsql是Python中操作MySQL的模块，其使用方法和MySQLdb几乎相同。
	但目前pymysql支持python3.x而后者不支持3.x版本
	参考博客：https://www.cnblogs.com/wt11/p/6141225.html
'''


con = pymysql.connect(
    host='localhost',
    port=3306,
    user='benf',
    passwd='',
)
#建立游标cursor
cursor = con.cursor()
db = 'test'
createDBsql = 'create database if not exist %s'%db
cursor.execute(createDBsql)
#fetch数据默认是元祖类型
db = cursor.fetchall()
#游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#获取执行完存储的参数,参数@开头
cursor.execute("select @p1,@_p1_1,@_p1_2,@_p1_3")  

#sql 注入语句  ***
sql="select user,pass from tb7 where user='%s' and pass='%s'" % (user,passwd)

#使用pymysql提供的参数化语句防注入  excute执行SQL语句的时候，必须使用参数化的方式，否则必然产生SQL注入漏洞。
cursor.execute("select user,pass from tb7 where user=%s and pass=%s",(user,passwd))

# 提交，不然无法保存新建或者修改的数据
conn.commit()
  
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1',charset='utf8'):
  conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
  cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
  try:
    yield cursor
  finally:
    conn.commit()
    cursor.close()
    conn.close()
 
# 执行sql
with mysql() as cursor:
  print(cursor)
  row_count = cursor.execute("select * from tb7")
  row_1 = cursor.fetchone()
  print row_count, row_1