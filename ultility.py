import re

#找到字符串中最后一个相同字符位置
def FindThelastcharpoint(Str1,findchar):
    nPos = -1
    #字符串取反
    Str2 = Str1[::-1]
    #print (Str2)
    for c in Str2:
        if c == findchar:
            nPos = Str2.index(c)
            continue
    if nPos != -1:
        return len(Str1)-nPos
    else:
        return -1

#根据当前路径获取上一条路径
def GetLastPath(CurPath):
    TheLastCharPoint = FindThelastcharpoint(CurPath,'/')
    if(TheLastCharPoint != -1):
        LastPath = CurPath[0:TheLastCharPoint-1]
        return LastPath
    else:
        return -1


#获取字符串中的数字
def GetNumFromString(Str):
    Num = re.sub(r"\D","",Str)
    return Num

#字符串中找字符串判断
def StringInString(StrLong,StrShort):
    try:
        nPos = StrLong.index(StrShort)
        return nPos
    except:
        return -1
        
