import requests
import time
i = 0
c = 1
n = input("How many classes do you want to give:")
for i in range(0,int(n)):
    payload = {
        'pageIndex': 1,
        'pageSize:': 50,
        'relativeOffset': 0,
        'searchTimeType': -1,
        'orderType': 50,
    }
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/91.0.4472.77 Safari/537.36'
    }
    url = 'https://study.163.com/j/search/hotwords.json?hotwordType=0'
    response = requests.post(url, headers=headers, json=payload)
    g = response.json()
    print(c,' ',g['result']['recomHotword'][1]['name'],':',g['result']['recomHotword'][1]['url'])
    c = c + 1
    time.sleep(1)
 
 
