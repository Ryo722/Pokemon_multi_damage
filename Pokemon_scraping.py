# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 全国図鑑番号の末尾．
# 8世代はバドレックスの898
Max_dex = 898

# 参照したいURLのベース．ここに図鑑番号をくっけて個別ページを巡回する
url = "https://pokemondb.net/pokedex/"
for i in range(Max_dex):
    # アクセスしたいURLを生成
    url += str(i)

    # Responseオブジェクト生成
    response = requests.get(url)
    # 文字化け防止
    response.encoding = response.apparent_encoding
    # BeautifulSoupオブジェクト生成
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.find_all("div", id='main')
    print(elems)

    #statetab = soup.find(class_="tabset-basics.sv-tabs-wrapper.sv-tabs-onetab")
    #print(statetab.text)

    #.tabset-basics
    #table = soup.findAll("table", {"class":"tablesorter"})[0]

    # 取得したデータを記録
    #f = open('PokeDB.csv', 'w')

    # タグの取得