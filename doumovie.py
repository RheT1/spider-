#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import lxml
import time
import pymysql

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
url_list=[]	
item_list=[]	
title=[]
socre=[]
comment_list=[]	
em=[]
#获取整个TOP250的网址	
for i in range(1,11):
	m = 25*(i-1)
	url = "https://movie.douban.com/top250?start=%d&fileter="%m
	url_list.append(url)
#先获取一个页面的关键元素，在将所有页面的分别整合在各自的list中
for j in range(0,10):	
	html = requests.get(url_list[j],headers=headers,timeout=5)
	html.encoding = 'utf-8'
	html1 = html.content
	soup = BeautifulSoup(html1,'lxml')
	items = soup.find_all("div",attrs={"class":"item"})
	for item in items:
		title.append(item.find("span",attrs={"class":"title"}).get_text())
		socre.append(item.find("span",attrs={"class":"rating_num"}).get_text())
		em.append(item.find("em").get_text())
		comment=(item.find("span",attrs={"class":"inq"}))
		#判断是否有短评
		if comment:
			comment_list.append(comment.get_text())
		else:
			comment_list.append("无")
	#增加访问下一个页面延时，防止速度过快，导致被封ip	
	time.sleep(2)
#在windows下面，新文件的默认编码是gbk，这样的话，python解释器会用gbk编码去解析
#我们的网络数据流txt，然而txt此时已经是decode过的unicode编码，
#这样的话就会导致解析不了，出现上述问题。 解决的办法就是，改变目标文件的编码	

for k in range(len(title)):
	item_list.append([title[k],socre[k],comment_list[k]])
conn = pymysql.connect(host='127.0.0.1',user='root',password='xbq950901',db='mysql',charset='utf8mb4')
cur = conn.cursor()

cur.execute('use scraping')
cur.execute('drop table if exists movies')
createTable = """create table movies(
              id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
			  title char(255) not null,
			  socre char(4),
			  comment char(255)
			  )"""
cur.execute(createTable)
sql = "INSERT INTO movies(title,socre,comment) values(%s,%s,%s)"
cur.executemany(sql,item_list)
conn.commit()

print("Finsh")
cur.close()
conn.close()
	
