# GETリクエスト
import requests

html = requests.get("https://aiacademy.jp/assets/scraping/sample1.html").text

from bs4 import BeautifulSoup
 
# HTMLを解析
soup = BeautifulSoup(html, 'html.parser')
 
# 解析したHTMLから任意の部分のみを抽出（ここではtitleとbody）
title = soup.find("title")
body = soup.find("body")
 
print("title: " + title.text)
print("body: " + body.text)