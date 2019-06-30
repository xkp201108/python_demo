import requests
from bs4 import BeautifulSoup
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
word = str(input("input the word you want to search:"))
response = requests.get("https://www.baidu.com/s?ie=UTF-8&wd={0}".format(word),headers = headers).content
list = []
soup = BeautifulSoup(response,"html.parser")
for i in soup.find_all('h3',class_='t'):
    result = str(i.find("a"))
    l = re.findall(r'<em>(.*?)</em>(.*?)</a>',result)
    if l:
        l = str(l[0][0])+str(l[0][1])
        index = l.find('<em>')
        index2 = l.find("</em>")
        if index!=-1:
           l = l[:index]+l[index+4:index2]+l[index2+5:]
        list.append(l)
print(list[0:3])