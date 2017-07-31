#!/usr/bin/python3
# -*- coding:utf-8 -*-
import itchat
import csv


itchat.login()
friends = itchat.get_friends(update=True)[0:]
#male = female = other = 0
#for i in friends[1:]:
#	sex = i['Sex']
#	if sex == 1:
#		male += 1
#	elif sex == 2:
#		female += 1
#	else:
#		other += 1
#total = len(friends[1:])
#print("male:%.2f%%" % (float(male)/total*100) + "\n" +
#"female:%.2f%%" % (float(female)/total*100) + "\n" +
#"other:%.2f%%" % (float(other)/total*100))
data = []
def get_var(var):
	variable = []
	for i in friends:
		value = i[var]
		variable.append(value)
	return variable
NickName = get_var("NickName")
Sex = get_var("Sex")
Province = get_var("Province")
City = get_var("City")
Signature = get_var("Signature")
 
for i in range(len(NickName)):
	data.append([NickName[i],Sex[i],Province[i],City[i],Signature[i]])
	
with open('file.csv','w',newline='',encoding='utf-8-sig') as f:
	writer = csv.writer(f)
	writer.writerows(data)

