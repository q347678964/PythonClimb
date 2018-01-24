#!/usr/bin/python3
 
import pymysql
import time


def open(database_name):
   # 打开数据库连接
   db = pymysql.connect("localhost","root","13534147913",database_name )
   #print(db)
   return db




def test(database):
   cursor = database.cursor()
   # 使用 execute()  方法执行 SQL 查询 
   cursor.execute("SELECT VERSION()")
   # 使用 fetchone() 方法获取单条数据.
   data = cursor.fetchone()
   print ("Database version : %s " % data)




def createtable(database,tablename):
   cursor = database.cursor()
   sqlcmd = "DROP TABLE IF EXISTS %s"%tablename
   #print (sqlcmd)
   cursor.execute(sqlcmd)
   
   '''
   sqlcmd = """CREATE TABLE %s (
            FIRST_NAME  CHAR(20) NOT NULL,
            LAST_NAME  CHAR(20),
            AGE INT,  
            SEX CHAR(1),
            INCOME FLOAT )"""%tablename
   
   '''
   sqlcmd = """CREATE TABLE %s (
   ID INT,
   TIME CHAR(20) NOT NULL,
   URL CHAR(200) NOT NULL,
   DIRPATH CHAR(200))"""%tablename
   
   #print (sqlcmd)
   cursor.execute(sqlcmd)




def insert(database,tablename,urlid,url):
   #print(database)
   cursor = database.cursor()
   # SQL 插入语句
   '''
   sqlcmd = """INSERT INTO %s(FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""%tablename
   '''
   curtime = time.strftime('%H:%M:%S',time.localtime(time.time()))
   sqlcmd = """INSERT INTO %s(ID,TIME,URL)
            VALUES (%d,'%s','%s')"""%(tablename,urlid,curtime,url)
   
   #print (sqlcmd)
   try:
      # 执行sql语句
      cursor.execute(sqlcmd)
      # 提交到数据库执行
      database.commit()
   except:
      # 如果发生错误则回滚
      print ('unable to write data')
      database.rollback()

def update(database,tablename,url,dirpath):
   cursor = database.cursor()
   sqlcmd = """UPDATE %s SET DIRPATH ='%s' WHERE URL = '%s'"""%(tablename,dirpath,url)
   #print (sqlcmd)
   
   try:
      cursor.execute(sqlcmd)
      database.commit()
   except:
      print ('unable to update data')
      database.rollback()

def read(database,tablename,urlid):
   cursor = database.cursor()
   # SQL 查询语句
   '''
   sqlcmd = "SELECT * FROM ClimbURL WHERE INCOME > '%d'" % (1000)
   '''
   sqlcmd = """SELECT * FROM %s WHERE ID = '%d'""" % (tablename,urlid)

   #print(sqlcmd)
   try:
      # 执行SQL语句
      cursor.execute(sqlcmd)
      # 获取所有记录列表
      results = cursor.fetchall()
      for row in results:
         idid = row[0]
         time  = row[1]
         urlurl = row[2]
          # 打印结果
         #print ("idid=%d,urlurl=%s" % (idid, urlurl ))
         return urlurl
   except:
      print ("Error: unable to fetch data")
      return -1
   return -1

def find(database,tablename,url):
   cursor = database.cursor()
   # SQL 查询语句
   sqlcmd = """SELECT * FROM %s WHERE URL = '%s'""" % (tablename,url)
   #print(sqlcmd)
   try:
      cursor.execute(sqlcmd)
      results = cursor.fetchall()
      for row in results:
         idid = row[0]
         time  = row[1]
         urlurl = row[2]
         #print ("idid=%d,urlurl=%s" % (idid, urlurl ))
         return idid
      
   except:
      print ("Error: unable to fetch data")
      return -1
   return -1


def close(database):
   # 关闭数据库连接
   database.close()
