# GETリクエスト
import requests
import sys # python hoge.py arg1 arg2...   arg1 = sys.argv[1] 
import os
from bs4 import BeautifulSoup

def main():
    targetUrllist = [1, 2, 3]  #初期化 new,sales1,sales2
    # if(len(argv)<2):
    #     print("python3 main.py $名前$\n と入力してね")
    #     return
    # name = sys.argv[1]
    # path = './pic/'+name
    path = './sorces/hoge'
    print("aaa")

    # if not os.path.isdir(path):
    #     print('aaa')
    #     os.makedirs(path)

    """

    for tUrl in len(targetUrllist): #See https://qiita.com/motoki1990/items/d06fc7559546a8471392
        urlName = "https://prcm.jp/list/"+name+"?page={}".format(i+1) #Change!!
        url = requests.get(tUrl)
        soup = BeautifulSoup(url.content, "html.parser")
        
        img_list = soup.select('div>ul>li>a>div>img') #Change!!
        explain_list = soup.select('div>ul>li>a>div>img') #Change!!
        hoge_list = soup.select('div>ul>li>a>div>img') #Change!!

        
    def download_img(url, file_name): # if img  
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(r.content)
    """

    html = requests.get("https://aiacademy.jp/assets/scraping/sample1.html").text
    
    # HTMLを解析
    soup = BeautifulSoup(html, 'html.parser')
    
    # 解析したHTMLから任意の部分のみを抽出（ここではtitleとbody）
    title = soup.find("title")
    body = soup.find("body")
    
    print("title: " + title.text)
    print("body: " + body.text)

    # links = soup.find_all("a")
    
    # for a in links:
    #     href = a.attrs['href']
    #     text = a.text
    #     print(text, href)
        
if __name__ == '__main__':
    main() 