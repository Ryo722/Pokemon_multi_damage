# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import numpy as np

#from selenium import webdriver

'''
#Firefoxを操作
driver = webdriver.Firefox()
driver.get('https://pokemondb.net/pokedex/all')
'''


# 全国図鑑番号の末尾．
# 8世代はバドレックスの898
Max_dex = 898

# 参照したいURL
url = "https://pokemondb.net/pokedex/all"

# Responseオブジェクト生成
response = requests.get(url)
# 文字化け防止
response.encoding = response.apparent_encoding
# BeautifulSoupオブジェクト生成
soup = BeautifulSoup(response.text, "html.parser")

# 図鑑番号と名前を含むタグを取得
elems = soup.select('#pokedex tr td .infocard-cell-data, #pokedex tr td .ent-name')

# 図鑑番号とポケモンの名前の文字列を取得
dex_and_name = []
for elem in elems:
    dex_and_name.append(elem.string)

# リストを整形
dex_and_name2 = []
for i in range(0, len(dex_and_name), 2):
    dex_and_name2.append(dex_and_name[i:i+2])

# 取得したデータを記録
f = open('Pokedex_and_name.txt', 'w')
for line in dex_and_name2:
    f.write(line[0] + ' ' + line[1] + '\n')



'''
for i in range(Max_dex):
    # アクセスしたいURLを生成
    url += str(i)

    # Responseオブジェクト生成
    response = requests.get(url)
    # 文字化け防止
    response.encoding = response.apparent_encoding
    # BeautifulSoupオブジェクト生成
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table")
    print(table)
    #elems = soup.find_all("div", id='main')
    #print(elems)

    #statetab = soup.find(class_="tabset-basics.sv-tabs-wrapper.sv-tabs-onetab")
    #print(statetab.text)

    #.tabset-basics
    #table = soup.findAll("table", {"class":"tablesorter"})[0]

    # 取得したデータを記録
    #f = open('PokeDB.csv', 'w')

    # タグの取得
'''