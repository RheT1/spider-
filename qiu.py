#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import sys
import os
 
#page = 1
url = 'https://www.qiushibaike.com/text/' 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
response = requests.get(url,headers=headers)
response.encoding='utf-8'
soup = BeautifulSoup(response.content,'lxml')
items = soup.find_all("div",attrs={"class":"content"})

#length = len(items)
#for j in range(0,length):
#	f = open("file.txt","w") 
#	f.write(str(j+1)+':')
#	f.write(items[j].get_text())
#	f.write("\n")
	#f.close()
		
with open("filename.txt","w") as f:
	for item in items:
		f.write(item.get_text())
		f.write("\n")
		#print (item.get_text())
		