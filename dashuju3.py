import requests
import bs4
import csv

from lxml import etree
import requests
import  time
import os

import datetime
import time
#创建或者写入csv
csv_file=open('dashuju250.csv', 'w', newline='',encoding='utf-8')
writer = csv.writer(csv_file)
#列名添加
writer.writerow(['No', 'name', 'score', 'recommendation', 'yanyuan','daoyan','year','country','classes'])
#请求头越猛越好，反正这个豆瓣就是让你爬的，不用那么多也行
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': 'lang=zh-cn; theme=default; ajax_lastNext=on; selfClose=1; bugModule=0; bugBranch=0; treeBranch=0; moduleBrowseParam=0; openApp=qa; windowWidth=659; windowHeight=706',
    }
#因为有十个页面，所以目前采用分别爬取
for x in range(10):
    #每一个的连接
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    #靓汤出马
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    #就打开f12找需要的东西的<li>在哪
    for titles in bs.find_all('li'):
        print(titles)
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        others=titles.find('div',class_='bd').find('p').text.strip('').split('\n')

        if '\xa0\xa0\xa0' in others[1]:
            actors_director=others[1].strip('').split('\xa0\xa0\xa0')
            director=actors_director[0].strip(' ')
            actors=actors_director[1]
        else:
            actors_director=others[1].strip('').split('\xa0\xa0\xa0')
            director=actors_director[0].strip(' ')
            actors=''

        year_country_type=others[2].strip('').split('\xa0/\xa0')
        year=year_country_type[0].strip(' ')
        country=year_country_type[1]
        movie_type=year_country_type[2]
        #对于可能存在的空数据，可以用if/else语句分情况讨论，这样就不会无法运行或者碰到数据不完整的情况了
        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            writer.writerow([num , title , comment , tes , actors,director, year, country, movie_type])
        else:
            writer.writerow([num , title , comment , '', actors,director, year, country, movie_type])   
#关上罪恶的文件
csv_file.close()
