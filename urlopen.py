import requests  
header = {
 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Connection':'keep-alive'
}

def tryopen(UrlParameter):
    try:
        r = requests.get(UrlParameter,headers=header,timeout=3)
    except Exception:
        data = {
            'url':UrlParameter,
            'error_type':'requests.get.error'
        }
        #print(data)
        return -1
    else:
        try:
            r.raise_for_status()
        except:
            data = {
                'url':UrlParameter,
                'error_type':'requests.status.error'
            }
            #print(data)
            return -1
        else:
            return r
