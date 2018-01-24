#import cStringIO, urllib2, Image

def FindThelastcharpoint(Str1,findchar):
    nPos = -1
    #字符串取反
    Str2 = Str1[::-1]
    print (Str2)
    for c in Str2:
        if c == findchar:
            nPos = Str2.index(c)
            continue
    if nPos != -1:
        return len(Str1)-nPos
    else:
        return -1


def GetLastPath(CurPath):
    TheLastCharPoint = FindThelastcharpoint(CurPath,'/')
    if(TheLastCharPoint != -1):
        LastPath = CurPath[0:TheLastCharPoint-1]
        return LastPath
    else:
        return -1

def GetPictureSize(Path):
    url = 'http://www.01happy.com/wp-content/uploads/2012/09/bg.png'
    file = urllib2.urlopen(url)
    tmpIm = cStringIO.StringIO(file.read())
    im = Image.open(tmpIm)

    print (im.format, im.size, im.mode)
