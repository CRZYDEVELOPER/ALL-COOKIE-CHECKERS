from randomproxy import random_proxy
def check_userpass(prox):
    prox = str(prox).strip()  
    parts = prox.split(":")
    
    if len(parts) == 4:
        username = parts[2]
        password = parts[3]
        proxy_url = {
            "https": f"http://{username}:{password}@{parts[0]}:{parts[1]}",
            "http": f"http://{username}:{password}@{parts[0]}:{parts[1]}"
        }
    else:
        proxy_url = {
            "https": f"http://{prox}",
            "http": f"http://{prox}"
        }
    
    return proxy_url

def conn(obj, url,filesname, headers=None, files=None,params=None, json=None, data=None, cookies=None, timeout=1000, allow_404=False,verify=False):
        conn_counter = 20
        while conn_counter > 0:
            try:
                proxy = check_userpass(random_proxy(filesname))
                if not headers:
                    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
                r = obj(url=url, headers=headers, params=params, data=data, cookies=cookies,
                  proxies=proxy,
                  json=json,
                  timeout=timeout,verify=verify,files=files)
                if allow_404:
                    if r.status_code == 404:
                        return r
                if r.status_code is not None:
                    return r
                conn_counter -= 1
            except Exception as e:
                try:
                    conn_counter -= 1
                    continue
                finally:
                    e = None
                    del e
