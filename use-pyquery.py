#导入
import requests
from pyquery import PyQuery as pq
#获取内容
url = 'https://www.csdn.net/?spm=1018.2226.3001.4476'
html = requests.get(url)
html_text = html.text
pq_str = pq(html_text)
pq_get = pq_str('.title')
print(pq_get.text())
