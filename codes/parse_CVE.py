import re
import requests
import threading
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip,deflate,br',
    'Connection': 'Upgrade',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'User-Agent': None,
}
URL = 'https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword='


def cve_handler(package):
    cve_url_list = find_CVE_url(package)
    res = []
    for cve_url in cve_url_list:
        res.extend(find_CVE(cve_url))
    return (package[0], res)


def find_CVE_url(package):
    url = URL + package[0]
    if package[1]:
        url = url + '+' + package[1]

    page_url = 'https://nvd.nist.gov'
    rps = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(rps.text, features="html.parser")
    tags = soup.find_all('a', attrs={'class': 'btn btn-sm'})
    res = []
    for tag in tags:
        href = tag['href']
        CVE_url = page_url + href
        res.append(CVE_url)
    return res


def find_CVE(CVE_url):
    CVE_table = []
    rps = requests.get(CVE_url, headers=HEADERS)
    soup = BeautifulSoup(rps.text, features="html.parser")
    tags = soup.find_all('tr', attrs={'data-testid': True})
    severity_pattern = re.compile(r'(V3.+?)\s+(V2.+?)\n')
    for tag in tags:
        cve_info = tag.contents
        cve_id = cve_info[1].get_text()
        cve_summary = cve_info[3].get_text()
        cve_severity_string = cve_info[5].get_text()
        cve_severity_match = re.search(severity_pattern, cve_severity_string)
        CVE_table.append([cve_id, cve_summary, cve_severity_match.group(
            1), cve_severity_match.group(2)])
    return CVE_table


def parse_CVE(package_list):
    # param
    # [('numpy', 'version'), ]
    # return
    # cve_dict
    # {'numpy':[[cve_id, cve_summary, cve_v3, cve_v2], ], 'requests':..}
    with ThreadPoolExecutor(max_workers=4) as pool:
        cve_list = pool.map(cve_handler, package_list)
        cve_dict = dict(cve_list)
    return cve_dict

if __name__ == '__main__':
    package_list = [('numpy', '1.8.1'), ('requests', '2.0.1')] #tuple
    package_list = [('org', '5.0.0'), ('flask', '2.1.2')]
    cve_dict = parse_CVE(package_list)
    print (cve_dict)
