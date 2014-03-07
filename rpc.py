#!/usr/bin/python
#encoding=utf-8

import xmlrpclib

url = "http://ppzone.sinaapp.com/xmlrpc.php"
server = xmlrpclib.ServerProxy(url)
title="使用python发布wordpress博文"
content='''
原文如下：
http://www.jansipke.nl/using-python-to-add-new-posts-in-wordpress/
代码如下：

import datetime, xmlrpclib

wp_url = “http://www.example.com/xmlrpc.php”
wp_username = “someuser”
wp_password = “secret”
wp_blogid = “”

status_draft = 0
status_published = 1

server = xmlrpclib.ServerProxy(wp_url)

title = “Title with spaces”
content = “Body with lots of content”
date_created = xmlrpclib.DateTime(datetime.datetime.strptime(“2009-10-20 21:08″, “%Y-%m-%d %H:%M”))
categories = ["somecategory"]
tags = ["sometag", "othertag"]
data = {‘title’: title, ‘description’: content, ‘dateCreated’: date_created, ‘categories’: categories, ‘mt_keywords’: tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)

核心思想，就是通过wordpress的XML RPC通信接口来实现发文。
'''
data = {'title':title,
		'description':"description test",
		'categories':[''],
		'mt_keywords':["tag1",'tag2'],
		'post_status':'publish',
		'date_created':'1926-10-26 12:23:45'
}
wp_uid="strivescript"
wp_passwd="aniceday"
print server.metaWeblog.newPost('',wp_uid,wp_passwd,data,0)

