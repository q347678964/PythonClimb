import GetHtml
import time
import mysqlop
import re
import ultility
import os
import shutil
g_WebKeyString = "mmonly"
g_Web = "http://www.mmonly.cc"
#g_Web = "http://www.mmonly.cc/ktmh/mhrw/189164.html"
g_pDataBaseName = 'testdb'
g_pTableName = 'urllist'
g_SaveDir = ".\\output"
##################获取当前系统时间
Curtime = time.time()
CurtimeString = time.strftime('%H:%M:%S',time.localtime(Curtime))
CurtimeString = 'Spider Start at:' + CurtimeString
print (CurtimeString)
##################打开数据库,创建urllist表
pDataBase = mysqlop.open(g_pDataBaseName)
mysqlop.test(pDataBase)
mysqlop.createtable(pDataBase,g_pTableName)
##################
#爬完首页之后所有URL都会写入到数据库testdb的urllist表中
#################删除输出目录
if os.path.exists(g_SaveDir) == True:
    shutil.rmtree(g_SaveDir)
os.mkdir(g_SaveDir)
#################
MainHTMLDir = g_SaveDir + '\\MainDir'
mysqlop.insert(pDataBase,'urllist',0,g_Web,'NoClimb')
mysqlop.close(pDataBase)
GetHtml.ClimbHtml(g_Web,MainHTMLDir)

pDataBase = mysqlop.open(g_pDataBaseName)
urlnum = mysqlop.getitemnum(pDataBase,g_pTableName)
print('Total urlnum = %d'%urlnum)
#跳过MainDir.ID为0是MainDir,从表单ID为1开始爬.
g_CurUrlID = 1

while 1:
    if(g_CurUrlID < urlnum):
        #爬一次读取到的URL数量
        savepath = g_SaveDir + "\\out%d"% g_CurUrlID
        Cururl = mysqlop.read(pDataBase,g_pTableName,g_CurUrlID)
        print('----------------------------------------')
        #print('SavePath = [%s]'%savepath)   
        print('Climbing [%s] ...'%Cururl)
        #URL中能找到关键字，才爬
        nps = ultility.StringInString(Cururl,g_WebKeyString)
        if Cururl != -1 and nps != -1:
            GetHtml.ClimbHtml(Cururl,savepath)
        g_CurUrlID = g_CurUrlID + 1   
    else:
        #关闭再打开，用于刷新数据库，不然读出来的数量不会变
        mysqlop.close(pDataBase)
        pDataBase = mysqlop.open(g_pDataBaseName)
        #数据不够了，继续从数据库中读
        urlnum = mysqlop.getitemnum(pDataBase,g_pTableName)
        print('urlnum=%d,g_CurUrlID=%d'%(urlnum,g_CurUrlID))
        #读出来的数据和当前UrlID相同说明已经没有数据了
        if urlnum == g_CurUrlID:
            print('urlnum=%d,g_CurUrlID=%d'%(urlnum,g_CurUrlID))
            break;

mysqlop.close(pDataBase)
print('Spider Over')
