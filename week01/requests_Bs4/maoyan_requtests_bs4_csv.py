# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import lxml
import csv

header = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://maoyan.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://maoyan.com/films?showType=3',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
# url = "https://maoyan.com/films?showType=3"
# response = requests.get(url, headers=header)
# # print(response.status_code)
# htm = response.text

with open('maoyan.html', 'r', encoding='UTF-8') as url_local:
    bs_info = bs(url_local, 'html.parser')
#利用bs4 解析页面代吗
film_name = []
film_actor = []
film_type = []
film_first_time = []
film_hover = []
for tags in bs_info.find_all('div', attrs={'class':'movie-hover-info'},limit=10):
    # print(tags)
    for atag in tags.find_all('span', attrs={'class':'name'}):
        film_name.append(atag.text)
    # print(tags.find_all('类型'))
    for atag_type in tags.find_all('span', attrs={'class':'hover-tag'}):
        film_hover.append(atag_type.next_element.next_element)
# print(len(film_hover))
for i in range(0, len(film_hover)-2, 3):
    film_type.append(film_hover[i].strip().rstrip('\n'))
    film_first_time.append(film_hover[i+2].strip().rstrip('\n'))
print(film_name)
print(film_type)
print(film_first_time)
out_list = zip(film_name, film_type, film_first_time)
# print(out_list)
with open('maoyan_movie.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    head = ['Name', 'Type', 'Date']
    writer.writerow(head)
    for data in out_list:
        writer.writerow(data)
        # writer.writerow(name)
# for k in range(len(film_name)):
#     writer(film_name[k], film_type[k], film_first_time[k])
#
