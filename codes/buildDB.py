import requests
from bs4 import BeautifulSoup

URL = "https://docs.python.org/zh-cn/3/py-modindex.html"
FILENAME = "standardDB.txt"
HEADER = {
        'Accept': '*/*', 
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 
        'Accept-Encoding': 'gzip,deflate,br', 
        'Connection': 'Upgrade', 
        'Cache-Control': 'no-cache', 
        'Pragma': 'no-cache', 
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)'
    }

def crawler():
    response = requests.get(url=URL, headers=HEADER, timeout=5)
    soup = BeautifulSoup(response.text, features="html.parser")
    tags = soup.findAll('code', attrs={"class":"xref"})
    with open(FILENAME, "w",encoding="utf-8") as f:
        for tag in tags:
            f.write(tag.string+'\n')

if __name__ == "__main__":
    crawler()