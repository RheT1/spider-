#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import lxml
import time
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
url_list=[]		
title_list=[]
socre=[]
comment_list=[]	
author=[]
#获取整个TOP250的网址	
for i in range(1,11):
	m = 25*(i-1)
	url = "https://book.douban.com/top250?start=%d"%m
	url_list.append(url)
#先获取一个页面的关键元素，在将所有页面的分别整合在各自的list中
for j in range(0,10):	
	html = requests.get(url_list[j],headers=headers,timeout=5)
	html.encoding = 'utf-8'
	html1 = html.content
	soup = BeautifulSoup(html1,'lxml')
	items = soup.find_all("table",attrs={"width":"100%"})
	for item in items:
		#title=item.find(re.compile("title")).get_title()
		title=item.div.a['title'] #抓取书名
		title_list.append(title)
		socre.append(item.find("span",attrs={"class":"rating_nums"}).get_text())
		author.append(item.find("p",attrs={"class":"pl"}).get_text())
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
f = open("book.txt","w",encoding='utf-8')
for k in range(len(title_list)):
	f.write(str(k+1)+"、"+"《"+title_list[k]+"》"+"  "+author[k])
	f.write("\n"+"\t"+socre[k]+"  "+comment_list[k])
	f.write("\n")	
f.close()
print("Finsh")
	
