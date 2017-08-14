# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import httplib
import urllib
import json
import MySQLdb
import time
import datetime

import rpc

#主要财务指标数据接口
reqHeader = rpc.getHeaders()

#参数
reqdata = {
	'symbol': 'SZ002561',
	'page': 1,
	'size': 1,
	'_': 1502605245564
}
data = urllib.urlencode(reqdata)

#连接服务器
conn = httplib.HTTPSConnection('xueqiu.com')
conn.request('GET', 'https://xueqiu.com/stock/f10/finmainindex.json?symbol=SZ002561&page=1&size=100&_=1502605245564', data, reqHeader)


#获取具体数据
resp = conn.getresponse()
status  = resp.status

if status != 200:
	print '请求数据失败'
	quit()

entity = resp.read();
decode = json.loads(entity)

#print decode

#遍历列表数据
for i in decode['list']:

	reportdate = i['reportdate'];
	
	if reportdate.find('0331') >= 0:
		print '季度：' + reportdate[0:4] + '年' + '1季度'
	elif reportdate.find('0631') >= 0:
		print '季度：' + reportdate[0:4] + '年' + '2季度'
	elif reportdate.find('0931') >= 0:
		print '季度：' + reportdate[0:4] + '年' + '3季度'
	else:
		print '季度：' + reportdate[0:4] + '年' + '4季度'

	print '报告日期: ' + str(i['reportdate'])
	print '每股收益：' + str(i['basiceps'])
	print '每股净资产: ' + str(i['naps'])
	print '每股现金流: ' + str(i['peropecashpershare'])
	print '每股经营现金流：' + str(i['peropecashpershare']) 
	print '净资产增长率：' + str(i['netassgrowrate'])
	print '净资产收益率(加权)(%): ' + str(i['weightedroe'])
	print '主营业务收入增长率(%): ' + str(i['mainbusincgrowrate'])
	print '净利润增长率：' + str(i['netincgrowrate'])
	print '总资产增长率(%): ' + str(i['totassgrowrate'])
	print '销售毛利率(%): ' + str(i['salegrossprofitrto'])
	print '主营业务收入: ' + str(i['mainbusiincome'])
	print '主营业务利润: ' + str(i['mainbusiprofit'])
	print '利润总额: ' + str(i['totprofit'])
	print '净利润: ' + str(i['netprofit'])
	print '资产总额: ' + str(i['totalassets'])
	print '负债总额：' + str(i['totalliab'])
	print '股东权益合计:' + str(i['totsharequi'])
	print '经营活动产生的现金流量净额: ' + str(i['operrevenue'])
	print '投资活动产生的现金流量净额: ' + str(i['invnetcashflow'])
	print '筹资活动产生的现金流量净额：' + str(i['finnetcflow'])
	print '现金及现金等价物净增加额: ' + str(i['cashnetr'])
	print '期末现金及现金等价物余额: ' + str(i['cashequfinbal'])


print ''
print 'end'


# 打开数据库连接
db = MySQLdb.connect('106.14.117.12', 'root', '123456', 'pengju_stock')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()


try:

	for i in decode['list']:
		sql = "INSERT INTO STOCK_FINANCIAL_INDEX(STOCK_CODE, INDEX_ID, CREATE_DATE, INDEX_NAME) \
			VALUES(%s, %d, %s, %s)" % ("002561", 1, i["reportdate"], " ")

		#操作数据库
		cursor.execute(sql)

except Exception, e:
	print e
	db.rollback()
finally:
	db.close();

