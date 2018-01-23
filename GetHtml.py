import requests  
import re
import GetJpg
import shutil
import os
OutputPicture = 1
OutputDir = '.\output'
CatChWeb = 'http://www.shuaige5.com'
#打开URL
r = requests.get(CatChWeb)
html = r.content
#html_doc=str(html,'utf-8')
html_doc=html.decode("utf-8","ignore")
#print (html_doc) 
fp = open("GetHtml_Log.txt","w",encoding='utf-8')  
fp.write(html_doc)
fp.close()

#删除输出目录
for i in range(1000):
    ExitDir = OutputDir + '%d'%i
    if os.path.exists(ExitDir) == True:
        shutil.rmtree(ExitDir)
'''
字符串位置查找
npos = html_doc.index('url')
print (npos)
print (html_doc.find("jpeg"))

'''
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
HtmlCounter = 0
link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,html_doc)
#for 循环是利用相同的缩进来作为一个整体{}
for url in link_list:
    if url[0] == '/':
        url = CatChWeb + url
    else:
        url = url
   
    urlall_fp.write(url)
    urlall_fp.write("\r\n")
    #找到*.html
    m =re.match(r"http://.+?\.html$|http://.+?\.htm$" ,url)
    if m:
        print (url) 
        urlhtml_fp.write(url)
        urlhtml_fp.write("\n")
        DirPath = OutputDir + '%d'%(HtmlCounter)
        HtmlCounter = HtmlCounter + 1
        if OutputPicture == 1:
            GetJpg.CatchJPG(url,DirPath)
        
    m =re.match(r"https://.+?\.html$|https://.+?\.htm$" ,url)
    if m:
        print (url) 
        urlhtml_fp.write(url)
        urlhtml_fp.write("\n")
        DirPath = OutputDir + '%d'%(HtmlCounter)
        HtmlCounter = HtmlCounter + 1
        if OutputPicture == 1:
            GetJpg.CatchJPG(url,DirPath)
        
    m =re.match(r"http://.+?\.com/$|http://.+?\.com$" ,url)
    if m:
        if url[len(url)-1] == '/':
            url = url[0:len(url)-1]
        print (url) 
        urlcom_fp.write(url)
        urlcom_fp.write("\n")
        DirPath = OutputDir + '%d'%(HtmlCounter)
        HtmlCounter = HtmlCounter + 1
        if OutputPicture == 1:
            GetJpg.CatchJPG(url,DirPath)
        
    m =re.match(r"https://.+?\.com/$|https://.+?\.com$" ,url)
    if m:
        print (url) 
        urlcom_fp.write(url)
        urlcom_fp.write("\n")
        DirPath = OutputDir + '%d'%(HtmlCounter)
        HtmlCounter = HtmlCounter + 1
        if OutputPicture == 1:
            GetJpg.CatchJPG(url,DirPath)
        
'''
    m =re.match(r"http://.+?\.com$" ,url)
    if m:
        urlcom_fp.write(url)
        urlcom_fp.write("\n")
'''
    
urlall_fp.close()
urlhtml_fp.close()
urlcom_fp.close()
