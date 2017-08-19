# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import httplib
import urllib
import json
import MySQLdb
import time
import datetime
import sys

import rpc

#主要财务指标数据接口
reqHeader = rpc.getHeaders()
print '更新股票财务数据:', str(sys.argv[1]), str(sys.argv[2])

#参数
reqdata = {
	'symbol': 'SZ002561',
	'page': 1,
	'size': 1,
	'_': 1502605245564
}
data = urllib.urlencode(reqdata)

stockMarket = sys.argv[1]
stockCode = sys.argv[2]
stockCodes = stockMarket + stockCode

#连接服务器
conn = httplib.HTTPSConnection('xueqiu.com')
conn.request('GET', 'https://xueqiu.com/stock/f10/finmainindex.json?symbol='+ stockCodes +'&page=1&size=500&_=1502605245564', data, reqHeader)

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
#for i in decode['list']:
	#reportdate = i['reportdate'];
	#if reportdate.find('0331') >= 0:
		#print '季度：' + reportdate[0:4] + '年' + '1季度'
	#elif reportdate.find('0631') >= 0:
		#print '季度：' + reportdate[0:4] + '年' + '2季度'
	#elif reportdate.find('0931') >= 0:
		#print '季度：' + reportdate[0:4] + '年' + '3季度'
	#else:
		#print '季度：' + reportdate[0:4] + '年' + '4季度'
	#print '报告日期: ' + str(i['reportdate'])
	#print '每股收益：' + str(i['basiceps'])
	#print '每股净资产: ' + str(i['naps'])
	#print '每股现金流: ' + str(i['peropecashpershare'])
	#print '每股经营现金流：' + str(i['peropecashpershare']) 
	#print '净资产增长率：' + str(i['netassgrowrate'])
	#print '净资产收益率(加权)(%): ' + str(i['weightedroe'])
	#print '主营业务收入增长率(%): ' + str(i['mainbusincgrowrate'])
	#print '净利润增长率：' + str(i['netincgrowrate'])
	#print '总资产增长率(%): ' + str(i['totassgrowrate'])
	#print '销售毛利率(%): ' + str(i['salegrossprofitrto'])
	#print '主营业务收入: ' + str(i['mainbusiincome'])
	#print '主营业务利润: ' + str(i['mainbusiprofit'])
	#print '利润总额: ' + str(i['totprofit'])
	#print '净利润: ' + str(i['netprofit'])
	#print '资产总额: ' + str(i['totalassets'])
	#print '负债总额：' + str(i['totalliab'])
	#print '股东权益合计:' + str(i['totsharequi'])
	#print '经营活动产生的现金流量净额: ' + str(i['operrevenue'])
	#print '投资活动产生的现金流量净额: ' + str(i['invnetcashflow'])
	#print '筹资活动产生的现金流量净额：' + str(i['finnetcflow'])
	#print '现金及现金等价物净增加额: ' + str(i['cashnetr'])
	#print '期末现金及现金等价物余额: ' + str(i['cashequfinbal'])

print ''
print 'end'


# 打开数据库连接
db = MySQLdb.connect('106.14.117.12', 'root', '123456', 'pengju_stock')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()


try:
	#删除数据
	sql = 'delete from stock_financial_index where stock_code = %s'
	cursor.execute(sql, (stockCode))
	db.commit

	for i in decode['list']:
		#新增数据
		sql = "insert into stock_financial_index(stock_code, index_id, create_date, index_name, index_value, index_season) VALUES(%s, %s, %s, %s, %s, %s)" 
		
		print str(i['reportdate']) + '数据更新'

		#季度计算
		reportdate = i['reportdate'];
		reportSeason = ''
		if reportdate.find('0331') >= 0:
			reportSeason = reportdate[0:4] + '年' + '1季度'
		elif reportdate.find('0631') >= 0:
			reportSeason = reportdate[0:4] + '年' + '2季度'
		elif reportdate.find('0931') >= 0:
			reportSeason = reportdate[0:4] + '年' + '3季度'
		else:
			reportSeason = reportdate[0:4] + '年' + '4季度'

		#操作数据库
		cursor.execute(sql, (stockCode, '1', i['reportdate'],  '每股收益', i['basiceps'], reportSeason))
		cursor.execute(sql, (stockCode, '2', i['reportdate'],  '每股净资产', i['naps'], reportSeason))

		#print '每股现金流: ' + str(i['peropecashpershare'])
		cursor.execute(sql, (stockCode, '3', i['reportdate'],  '每股现金流', i['peropecashpershare'], reportSeason))

		#print '每股经营现金流：' + str(i['peropecashpershare']) 
		cursor.execute(sql, (stockCode, '4', i['reportdate'],  '每股经营现金流', i['peropecashpershare'], reportSeason))

		#print '净资产增长率：' + str(i['netassgrowrate'])
		cursor.execute(sql, (stockCode, '5', i['reportdate'],  '净资产增长率', i['netassgrowrate'], reportSeason))

		#print '净资产收益率(加权)(%): ' + str(i['weightedroe'])
		cursor.execute(sql, (stockCode, '6', i['reportdate'],  '净资产收益率(加权)', i['weightedroe'], reportSeason))

		#print '主营业务收入增长率(%): ' + str(i['mainbusincgrowrate'])
		cursor.execute(sql, (stockCode, '7', i['reportdate'],  '净资产收益率(加权)', i['weightedroe'], reportSeason))		

		#print '净利润增长率：' + str(i['netincgrowrate'])
		cursor.execute(sql, (stockCode, '8', i['reportdate'],  '净利润增长率', i['netincgrowrate'], reportSeason))

		#print '总资产增长率(%): ' + str(i['totassgrowrate'])
		cursor.execute(sql, (stockCode, '9', i['reportdate'],  '总资产增长率', i['totassgrowrate'], reportSeason))

		#print '销售毛利率(%): ' + str(i['salegrossprofitrto'])
		cursor.execute(sql, (stockCode, '10', i['reportdate'],  '销售毛利率', i['salegrossprofitrto'], reportSeason))

		#print '主营业务收入: ' + str(i['mainbusiincome'])
		cursor.execute(sql, (stockCode, '11', i['reportdate'],  '主营业务收入', i['mainbusiincome'], reportSeason))

		#print '主营业务利润: ' + str(i['mainbusiprofit'])
		cursor.execute(sql, (stockCode, '12', i['reportdate'],  '主营业务利润', i['mainbusiprofit'], reportSeason))

		#print '利润总额: ' + str(i['totprofit'])
		cursor.execute(sql, (stockCode, '13', i['reportdate'],  '利润总额', i['totprofit'], reportSeason))

		#print '净利润: ' + str(i['netprofit'])
		cursor.execute(sql, (stockCode, '14', i['reportdate'],  '净利润', i['netprofit'], reportSeason))

		#print '资产总额: ' + str(i['totalassets'])
		cursor.execute(sql, (stockCode, '15', i['reportdate'],  '资产总额', i['totalassets'], reportSeason))

		#print '负债总额：' + str(i['totalliab'])
		cursor.execute(sql, (stockCode, '16', i['reportdate'],  '负债总额', i['totalliab'], reportSeason))

		#print '股东权益合计:' + str(i['totsharequi'])
		cursor.execute(sql, (stockCode, '17', i['reportdate'],  '股东权益合计', i['totsharequi'], reportSeason))

		#print '经营活动产生的现金流量净额: ' + str(i['operrevenue'])
		cursor.execute(sql, (stockCode, '18', i['reportdate'],  '经营活动产生的现金流量净额', i['operrevenue'], reportSeason))

		#print '投资活动产生的现金流量净额: ' + str(i['invnetcashflow'])
		cursor.execute(sql, (stockCode, '19', i['reportdate'],  '投资活动产生的现金流量净额', i['invnetcashflow'], reportSeason))

		#print '筹资活动产生的现金流量净额：' + str(i['finnetcflow'])
		cursor.execute(sql, (stockCode, '20', i['reportdate'],  '筹资活动产生的现金流量净额', i['finnetcflow'], reportSeason))

		#print '现金及现金等价物净增加额: ' + str(i['cashnetr'])
		cursor.execute(sql, (stockCode, '21', i['reportdate'],  '现金及现金等价物净增加额', i['cashnetr'], reportSeason))

		#print '期末现金及现金等价物余额: ' + str(i['cashequfinbal']) 
		cursor.execute(sql, (stockCode, '22', i['reportdate'],  '期末现金及现金等价物余额', i['cashequfinbal'], reportSeason))
		db.commit()
except Exception, e:
	print e
	db.rollback()
finally:
	print '数据更新完毕......'
	cursor.close()
	db.close();

