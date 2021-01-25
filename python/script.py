# GETリクエスト
from requests_html import HTMLSession
import sys # python hoge.py arg1 arg2...   arg1 = sys.argv[1] 
import os
import smtplib #mailer
from email.mime.text import MIMEText
#from bs4 import BeautifulSoup

def main():
    targetUrllist = [1, 2, 3]  #初期化 new,sales1,sales2
    # if(len(argv)<2):
    #     print("python3 main.py $名前$\n と入力してね")
    #     return
    # name = sys.argv[1]
    # path = './pic/'+name
    path = './sorces/'
    print("aaa")

    if not os.path.isdir(path):
        print('aaa')
        os.makedirs(path)

    url = "https://www.uniqlo.com/jp/ja/feature/limited-offers/men"

    # セッション開始
    session = HTMLSession()
    r = session.get(url)

    # ブラウザエンジンでHTMLを生成させる
    r.html.render()

    # スクレイピング
    mailCtx = ""
    product_name = r.html.find(".ocI5u4BRvjaH-uauZvJ8R > h3")
    for name in product_name:
        print(name.text)
        mailCtx += name.text + "\n"
        
    print("matometa" + mailCtx)
    mail(mailCtx)
    
    
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

    # html = requests.get("https://aiacademy.jp/assets/scraping/sample1.html").text
    
    # # HTMLを解析
    # soup = BeautifulSoup(html, 'html.parser')
    
    # # 解析したHTMLから任意の部分のみを抽出（ここではtitleとbody）
    # title = soup.find("title")
    # body = soup.find("body")
    
    # print("title: " + title.text)
    # print("body: " + body.text)

    # links = soup.find_all("a")
    
    # for a in links:
    #     href = a.attrs['href']
    #     text = a.text
    #     print(text, href)
def mail(content):
    smtp_host = 'smtp.gmail.com'
    smtp_port = 465
    username = 'python.sender.tester@gmail.com'
    password = 'iuhaotiqrwyodfel'
    from_address = 'python.sender.tester@gmail.com'
    to_address = 'python.sender.tester@gmail.com'
    subject = 'test subject'
    body = content
    charset = 'utf-8'
    
    msg = MIMEText(body.encode(charset), 'plain', charset)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
  
    
    # message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (from_address, to_address, subject, body))

    smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
    smtp.login(username, password)
    smtp.sendmail(from_address, to_address, msg.as_string()) 
    smtp.close()
            
if __name__ == '__main__':
    main() 