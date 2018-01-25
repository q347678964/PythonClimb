#抓图测试#####################################################

import requests  
import re
import GetJpg
OutputDir = '.\\output\\'
url = 'https://www.ivrfans.cn/meinvtupian/meinvzipai/92228_4.html'

DirPath = OutputDir

GetJpg.CatchJPG(url,DirPath)
GetJpg.CatchJPG(url,DirPath)
################################################################




#数据库测试#####################################################
'''
import mysqlop

pDataBase = mysqlop.open('testdb')
mysqlop.test(pDataBase)
mysqlop.createtable(pDataBase,'urllist')
mysqlop.insert(pDataBase,'urllist',1,'www.qq.com')
mysqlop.insert(pDataBase,'urllist',2,'www.baidu.com')
mysqlop.insert(pDataBase,'urllist',3,'www.hao123.com')
url = mysqlop.read(pDataBase,'urllist',2)
print(url)
result = mysqlop.find(pDataBase,'urllist','www.hao123.com')
print(result)
result = mysqlop.find(pDataBase,'urllist','www.none.com')
print(result)

mysqlop.update(pDataBase,'urllist','www.hao123.com','output1')

mysqlop.close(pDataBase)
'''
##############################################################




#多线程测试#####################################################
'''
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(self.arg)
        print ('the arg is:%s\r' % self.arg)

for i in range(4):
    t =MyThread(i)
    t.start()

print ('main thread end!')

import threading
import time
#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    time.sleep(arg)
    print ('the arg is:%s\r' %arg)

for i in range(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print ('main thread end!')
'''
#####################################################
