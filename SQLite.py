#导入SQLite驱动
import sqlite3

#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')

#创建一个Cursor
cursor = conn.cursor()

cursor.execute('create table user (id number (20) primary key,name varchar(20))')

#jacktao

