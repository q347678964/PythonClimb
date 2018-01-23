import requests  

def tryopen(UrlParameter):
    try:
        r = requests.get(UrlParameter)
    except Exception:
        data = {
            'url':UrlParameter,
            'error_type':'requests.get.error'
        }
        print(data)
        return -1
    else:
        try:
            r.raise_for_status()
        except:
            data = {
                'url':UrlParameter,
                'error_type':'requests.status.error'
            }
            print(data)
            return -1
        else:
            return r
