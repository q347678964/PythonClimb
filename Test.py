
import requests  
import re
import GetJpg
OutputDir = '.\output'
url = 'https://www.ivrfans.cn/meinvtupian/meinvzipai/92228_4.html'

DirPath = OutputDir

GetJpg.CatchJPG(url,DirPath)
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
