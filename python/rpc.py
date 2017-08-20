# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import httplib
import urllib
import MySQLdb
import json

#获取头部
def getHeaders():
	reqHeader = {
		'Host': 'xueqiu.com',
		'Cookie': 'device_id=66c2d36007ff06e2686dc5555681b887; s=g413wj53q7; aliyungf_tc=AQAAAFPxfG0WqwgA69CctG0k+/Ae9blI; xq_a_token=35967e90fece12b70f15096c72ae9b6982f628a7; xq_a_token.sig=-qUrmkra84xJqFAD2ZukbCZ1FMA; xq_r_token=04a34d441044eea56430a435d6c270f709b923ae; xq_r_token.sig=jIYThmOvEthGQpyKL58Zz9dXhE8; u=641503219881262; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1502715772,1502715919,1503102157,1503117111; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1503227448; __utma=1.484125305.1503102157.1503146711.1503227201.6; __utmb=1.4.10.1503227201; __utmc=1; __utmz=1.1503102157.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
	}
	return reqHeader

#获取JSON数据
def getResponse(url, method, data):
	#print url, method, data

	#连接服务器
	conn = httplib.HTTPSConnection('xueqiu.com')
	conn.request(method, url, data, getHeaders())

	#获取具体数据
	resp = conn.getresponse()
	status  = resp.status

	if status != 200:
		print '请求数据失败'
		quit()

	entity = resp.read();
	decode = json.loads(entity)
	return decode

#获取数据库连接
def getDBConnection(): 
	db = MySQLdb.connect('106.14.117.12', 'root', '123456', 'pengju_stock')
	return db

