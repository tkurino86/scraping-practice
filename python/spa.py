from requests_html import HTMLSession

url = "https://www.uniqlo.com/jp/ja/spl/collaboration/plusj/men/"

# セッション開始
session = HTMLSession()
r = session.get(url)

# ブラウザエンジンでHTMLを生成させる
r.html.render()

# スクレイピング
product_name = r.html.find(".ocI5u4BRvjaH-uauZvJ8R > h3")
for name in product_name:
    print(name.text)

