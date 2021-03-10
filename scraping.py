from bs4 import BeautifulSoup
import request
import pandas as pd
import time

url=""#ここにURLを
r=requests.get(url)
time.sleep(3)#リスポンス待つために
soup=BeautifulSoup(r.text,'html.parser')#HTMLの取得

#クラスから持ってくる
contens=soup.find(class_="")#classはclass_を使う

#タグから持ってくる
get_a=contens.find_all("a")#aタグの取得

#量を取得
len(get_a)
#リスト化
title_links=[]
for i in range(len(get_a)):
    try:
        linkget_a[i].get("href")
        title_links.append(link_)
    except:
        #リンク死んでいたとき
        pass

#CSV化