import requests
from bs4 import BeautifulSoup
URL = 'https://blog.csdn.net/Sunyoho?spm=1001.2014.3001.5343'
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
}
html = requests.get(url=URL, headers=head)
html.encoding = 'utf-8'
page = BeautifulSoup(html.text, 'lxml')
page.prettify()
print(page.title.string)
content = page.meta.next_sibling.next_sibling
print(content.attrs.get('content'))
