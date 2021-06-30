import requests
from bs4 import BeautifulSoup

# 全国図鑑番号の末尾．
# 8世代はバドレックスの898
Max_dex = 898

# 参照したいURLのベース．ここに図鑑番号をくっけて個別ページを巡回する
base_url = "https://pokemondb.net/pokedex/"

