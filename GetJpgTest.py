import requests  
import re
import GetJpg
OutputDir = '.\output'
url = 'http://www.7160.com/special/rentiyishu.html'

DirPath = OutputDir

GetJpg.CatchJPG(url,DirPath)


