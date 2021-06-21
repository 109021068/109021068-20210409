import requests as reqs
from bs4 import BeautifulSoup

url = 'https://csie.asia.edu.tw/zh_tw/project/project_105'
r = reqs.get(url, verify=False)
if r.status_code==200:
    f = open('output-projects.txt', 'w', encoding='utf8')
    soup = BeautifulSoup(r.content, 'html.parser')
    for div in soup.find_all('div', 'tab-pane'):
        f.write(div.find('h2').text+'\n')
        for tr in div.find_all('tr'):
            for td in tr.find_all('td'):
                f.write(td.text.replace('\t', '').replace('\n', '')+'\t')
            f.write('\n')
        f.write('\n')
    f.close()