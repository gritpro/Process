# 代码感受
import requests
r = requests.get("http://www.baidu.com")
r.status_code
r.encoding = 'utf-8'
r.text

# 多次爬取用时
import requests
import time
def getHTMLtext(url):
    try:
        r = requests.get(url,time = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if _name_=="_main_":
    url = "https://www.sina.com.cn"
    print(getHTMLtext(url))
    starttime = time.time()
    for i in range(101):
        getHTMLtext(url)
    endtime = time.time()
    dur = endtime - starttime
    print("爬取时间为{:.2f}s",format(dur))

# 京东商品页面的爬取
import  requests
url = "https://item.jd.com/100002795955.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")

# 亚马逊商品页面的爬取
import requests
url = "https://www.amazon.cn/dp/B01I6UG8WY?ref_=Oct_DLandingSV2_PC_df6829bb_0&smid=A3TEGLC21NOO5Y"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")

#百度搜索关键词提交
# 百度关键词接口：http://www.baidu.com/s?wd=keyword
# 360关键词接口：http://www.so.com/s?q=keyword
import requests
keyword = "python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")

# 网络图片的爬取
import requests
import os
url = "https://www.ivsky.com/download_pic.html?picurl=/img/tupian/pic/201811/23/huaping-009.jpg"
root = "D://pics//"
path = root + url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")

# ip地址归属地的查询
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(t.text[-500:])
except:
    print("爬取失败")
    
# beautiful soup库
import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')

#下行遍历
soup.head
soup.head.contents
soup.body.contents
len(soup.body.contents)
soup.body.contents[2]
for child in soup.body.children:
    print(child)  #遍历儿子节点

# 上行遍历
import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

soup.title.parent
soup.html.parent

#平行遍历
soup = BeautifulSoup(demo,'html.parser')
soup.a.next_sibling
soup.a.next_sibling.next_sibling

soup = BeautifulSoup(demo,'html.parser')
for sibling in soup.a.next_siblings:
    if parent is None:
        print(sibling)

for sibling in soup.a.previous_siblings:
    if parent is None:
        print(sibling)

# 信息提取的一般方法
import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

# 中国大学排名爬虫
import requests
from bs4 import BeautifulSoup
import bs4
def gethtmltext(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillunivlist(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printunivlist(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

def main():
    uinfo = []
    url = "https://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = gethtmltext()
    fillunivlist(uinfo,html)
    printunivlist(uinfo,20) #前20
main()
