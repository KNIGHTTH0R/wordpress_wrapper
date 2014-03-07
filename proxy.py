#!/usr/bin/python
#encoding=utf-8

import socks
import socket
import re
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"192.168.236.84",8068)
socket.socket = socks.socksocket
import urllib2,urllib
import xmlrpclib
import datetime
import sys

commit = 0 

def postHandle(url):
	html = urllib2.urlopen(url).read()
	html=html.replace("\n","")
	m =re.search('<a href="([^"]*)" rel="prev"',html)
	if m:
		result =  m.group(1)
		return result,html
	return "",html
	
def converge_html(html):
	title=""
	tags=""
	excerpt=""
	content=""
	cc = re.search(r'<div class="entry">(.*?)class="wpa"',html)
	if cc:
		content = cc.group(1)
	else:
		content=''
	tt = re.search(r'<h2 class="entry-title">(.*?)</h2>',html)
	if tt:
		title = tt.group(1)
	else:
		title=''
	return title,content
	
def xpc_client(wp_uid,wp_passwd,title,content):
	url = "http://ppzone.sinaapp.com/xmlrpc.php"
	server = xmlrpclib.ServerProxy(url)
	data = {'title':title,
			'description':content,
			'categories':[''],
			'mt_keywords':["tag1",'tag2'],
			'post_status':'publish',
			'date_created':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	}
	try:
		server.metaWeblog.newPost('',wp_uid,wp_passwd,data,0)
	except:
		return
	commit+=1
	print commit
	

if __name__ == "__main__":
	userinfo = {}
	print sys.argv
	userinfo['uid'] = sys.argv[1]
	userinfo['passwd'] = sys.argv[2]
	print userinfo
	url = "http://snowyrock.wordpress.com/2013/02/07/改进smarty使之能够定时自动清空缓存/"
	while(len(url) > 0 ):
		prev_url,body = postHandle(url)
		url = prev_url
		print url
		title,content = converge_html(body)
		if (len(title) < 1 or len(content) < 10):
			continue
		xpc_client(userinfo['uid'],userinfo['passwd'],title,content)
