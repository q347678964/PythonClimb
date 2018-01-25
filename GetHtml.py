import requests  
import re
import GetJpg
import shutil
import os
import mysqlop
import time
import urlopen
import ultility

#return -1网页无法打开
#return -2这个网页的图片无法加载
def ClimbHtml(WEB,SAVEDIR):
    OutputPicture = 1
    ################打开URL
    #print(WEB)
    #print(SAVEDIR)
    LastWeb = ultility.GetLastPath(WEB)
    #print('LastWeb = %s'%LastWeb)

    rep = urlopen.tryopen(WEB)
    if rep == -1:
        print('request failed.return -1')
        return -1
    #能够打开网页，删除SAVEDIR文件夹，创建文件夹SAVEDIR
    if os.path.exists(SAVEDIR) == True:
        shutil.rmtree(SAVEDIR)
    os.mkdir(SAVEDIR)
    
    #print('type = %s'%type(rep))
    #print('status_code = %s'%rep.status_code)
    #print('cookies = %s'%rep.cookies)
    #################

    #################解码HTML
    html = rep.content
    #html_doc=str(html,'utf-8')
    html_doc=html.decode("utf-8","ignore")
    #print (html_doc) 
    fp = open("GetHtml_Log.txt","w",encoding='utf-8')  
    fp.write(html_doc)
    fp.close()
    #################

    #################删除输出目录
    if os.path.exists(SAVEDIR) == True:
        shutil.rmtree(SAVEDIR)
    os.mkdir(SAVEDIR)
    #################
    '''
    字符串位置查找
    npos = html_doc.index('url')
    print (npos)
    print (html_doc.find("jpeg"))

    '''
    ##################打开数据库
    pDataBase = mysqlop.open('testdb') 
    ##################

    # 利用正则查找所有链接
    # $表示字符串末尾，^表示开头
    # *匹配前一个字符0或者无限次 >=0
    # +匹配前一个字符1或者无限次 >=1
    # ?匹配前一个字符0或者1次    0|1
    # .通配符，可以和*,+,?结合起来用
    # .+匹配任意无限的字符(至少有一个)
    # .*匹配任意无限的字符
    #(?<=...) 之前的字符串内容需要匹配...才行,可以理解为开头,不消耗字符串内容
    #(?=...) 之后的字符串内容需要匹配...才行,不一定是结尾,不消耗字符串内容
    # | 满足其中之一个正直表达式就行
    #下面的正直表达式的意思是提取href="..."之间的内容,或者href'...'之间的内容
    urlall_fp = open("GetHtml_url_all.txt","w",encoding='utf-8')
    urlhtml_fp = open("GetHtml_url_html.txt","w",encoding='utf-8')
    urlcom_fp = open("GetHtml_url_com.txt","w",encoding='utf-8')
    HtmlTotalCounter = 0
    link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,html_doc)
    #for 循环是利用相同的缩进来作为一个整体{}
    for url in link_list:
        if url[0] == '/':
            url = WEB + url
        else:
            url = url
       
        urlall_fp.write(url)
        urlall_fp.write("\r\n")
        #找http://*.html|htm
        ########################################################################
        m =re.match(r"http://.+?\.html$|http://.+?\.htm$" ,url)
        if m:
             #如果数据库中不存在该URL，将URL写入数据库，进行攀爬，防止爬虫进入死循环
            if mysqlop.find(pDataBase,'urllist',url) == -1:
                print (url)
                HtmlTotalCounter = mysqlop.getitemnum(pDataBase,'urllist')
                mysqlop.insert(pDataBase,'urllist',HtmlTotalCounter,url,'NoClimb')
                urlhtml_fp.write(url)
                urlhtml_fp.write("\n")
                HtmlTotalCounter = HtmlTotalCounter + 1
            continue
        ##########################################################################
        m =re.match(r"https://.+?\.html$|https://.+?\.htm$" ,url)
        if m:
            if mysqlop.find(pDataBase,'urllist',url) == -1:
                print (url)
                HtmlTotalCounter = mysqlop.getitemnum(pDataBase,'urllist')
                mysqlop.insert(pDataBase,'urllist',HtmlTotalCounter,url,'NoClimb')
                urlhtml_fp.write(url)
                urlhtml_fp.write("\n")
                HtmlTotalCounter = HtmlTotalCounter + 1
            continue
        #存在html后缀，但是没有http开头#########################################################################
        m =re.match(r".+?\.htm$|.+?\.html$" ,url)
        if m:
            if(url[0:3] != 'http'):
                url = LastWeb + '/' + url

            if mysqlop.find(pDataBase,'urllist',url) == -1:
                print (url)
                HtmlTotalCounter = mysqlop.getitemnum(pDataBase,'urllist')
                mysqlop.insert(pDataBase,'urllist',HtmlTotalCounter,url,'NoClimb')
                urlhtml_fp.write(url)
                urlhtml_fp.write("\n")
                HtmlTotalCounter = HtmlTotalCounter + 1
            continue
        ########################################################################
        m =re.match(r"http://.+?\.com/$|http://.+?\.com$" ,url)
        if m:
            if url[len(url)-1] == '/':
                url = url[0:len(url)-1]
                
            if mysqlop.find(pDataBase,'urllist',url) == -1:
                print (url)
                HtmlTotalCounter = mysqlop.getitemnum(pDataBase,'urllist')
                mysqlop.insert(pDataBase,'urllist',HtmlTotalCounter,url,'NoClimb')
                urlcom_fp.write(url)
                urlcom_fp.write("\n")
                HtmlTotalCounter = HtmlTotalCounter + 1
            continue
        ########################################################################           
        m =re.match(r"https://.+?\.com/$|https://.+?\.com$" ,url)
        
        if m:
            if mysqlop.find(pDataBase,'urllist',url) == -1:
                print (url)
                HtmlTotalCounter = mysqlop.getitemnum(pDataBase,'urllist')
                mysqlop.insert(pDataBase,'urllist',HtmlTotalCounter,url,'NoClimb')
                urlcom_fp.write(url)
                urlcom_fp.write("\n")
                HtmlTotalCounter = HtmlTotalCounter + 1
            continue
        ########################################################################
    
    #判断是否要进行图片解析
    if OutputPicture == 1:
        if GetJpg.CatChJpgThread(WEB,SAVEDIR) != -1:
            mysqlop.update(pDataBase,'urllist',WEB,SAVEDIR)
            return 0
        else:
            return -2
        
    urlall_fp.close()
    urlhtml_fp.close()
    urlcom_fp.close()
    mysqlop.close(pDataBase)
    return 0
