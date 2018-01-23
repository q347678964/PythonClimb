import os
import shutil
import requests  
import re
import time
import urlopen
  
def dowloadPic(imageUrl,filePath):
    r = requests.get(imageUrl)
    with open(filePath, "wb") as code:
        code.write(r.content)

def CatchJPG(UrlParameter,SaveDirPath):
#删除文件夹，创建文件夹
    if os.path.exists(SaveDirPath) == True:
        shutil.rmtree(SaveDirPath)
    os.mkdir(SaveDirPath)
    
    Python_URL = UrlParameter
    r = urlopen.tryopen(Python_URL)
    if r != -1:
        html = r.content


        #将byte类型转换为str类型
        #html_doc=str(html,'utf-8')
        html_doc=html.decode("utf-8","ignore")
        #print (html_doc) 

        fp = open("GetJpg_Log.txt","w",encoding='utf-8')  
        fp.write(html_doc)
        fp.close()

        # 利用正则查找所有链接
        # *匹配前一个字符0或者无限次 >=0
        # +匹配前一个字符1或者无限次 >=1
        # ?匹配前一个字符0或者1次    0|1
        # .通配符，可以和*,+,?结合起来用
        # .+匹配任意无限的字符(至少有一个)
        # .*匹配任意无限的字符
        # .+?匹配任意无限的字符，但是有?是贪婪模式,尽可能少的达到满足表达式要求.
        #(?<=...) 之前的字符串内容需要匹配...才行,可以理解为开头,不消耗字符串内容
        #(?=...) 之后的字符串内容需要匹配...才行,不一定是结尾,不消耗字符串内容
        # | 满足其中之一个正直表达式就行
        #下面的正直表达式的意思是提取href="..."之间的内容,或者href'...'之间的内容
        urljpg_fp = open("GetJpg_jpgurl.txt","w",encoding='utf-8')

        link_list = re.findall(r"(?<=src=\").+?\.jpg(?=\")|(?<=: \").+?\.jpg(?=\")" ,html_doc)

        jpgcounter = 0
        #for 循环是利用相同的缩进来作为一个整体{}
        for url in link_list:
            if url[0] == '/' and url[1] != '/':#当以/开始时，表示在当前网页的路径下找
                url = Python_URL + url
            elif url[0] == '/' and url[1] == '/':#当以//开头时，表示是一个新的网站地址
                urlhead = 'http://'
                url = url[2:len(url)]
                url = urlhead + url
            else:
                url = url
            #再度筛选，去除带有<alt><title>的路径
            npos = url.find('<')
            if npos >= 0:
                continue;
            #再度筛选，规避src="" src="***.jpg"的语法
            npos = url.find('\"')
            if npos >= 0:
                continue;
                
                          
            print (url)
                
            urljpg_fp.write(url)
            urljpg_fp.write("\n")
            jpgcounter = jpgcounter + 1
            filename = SaveDirPath + '\%d.jpg'%(jpgcounter)
            dowloadPic(url,filename)
            #请求一个图片之后，等待10ms,防止服务器反爬虫行为
            time.sleep(0.1)
            #未找到任何图片，删除创建的目录
        if(jpgcounter == 0):
            shutil.rmtree(SaveDirPath)
                
        urljpg_fp.close()
