#coding=gbk
import mysql.connector
import urllib2
import json
import time
import sys



config = {
	'user': 'demo',
	'password': 'demo',
	'host': 'localhost',
	'database': 'rui_site',
}

zrcaifu_url = 'https://www.zrcaifu.com/invest/detail?id='

var = u'中瑞财富'
str = var.encode('gbk')
print str
try:
	db = mysql.connector.connect(**config)
except Exception , e:
	print e;

for i in range(100,101):
        suffix = '' + `i`
        prefix = zrcaifu_url
        url = prefix +  suffix;
        try:
                print "start..." + suffix
                response = urllib2.urlopen(url)
                html = response.read()
                pos = html.find('123')
                html1 = html[pos:pos+100]
                print html1
        except Exception , e:
                print e

db.close()
