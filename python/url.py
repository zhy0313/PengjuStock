# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import httplib
import urllib
import json

#主要财务指标数据接口
reqHeader = {
	'Host': 'xueqiu.com',
	'Cookie': 'aliyungf_tc=AQAAAPqtyXxuKgcA4rJfZS86i/IcAJw+; s=eu1a0y8gx5; xq_a_token=b7445c1557f11e952f9b783240df9c9d7b58b7f1; xq_r_token=23dc6c96ff5f79ab8dcf0eb7d38db8d1842f739a; Hm_lvt_1db88642e346389874251b5a1eded6e3=1502699854; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1502699854; u=941502699853574; device_id=d969dc896ad8a8f880e82525c396bcb9'
}

#参数
reqdata={
	'symbol': 'SZ002561',
	'page': 1,
	'size': 1,
	'_': 1502605245564
}

data = urllib.urlencode(reqdata)
print(data);

#连接服务器
conn = httplib.HTTPSConnection('xueqiu.com')
conn.request('GET', 'https://xueqiu.com/stock/f10/finmainindex.json?symbol=SZ002561&page=1&size=100&_=1502605245564', data, reqHeader)

#获取具体数据
resp = conn.getresponse()
entity = resp.read();
decode = json.loads(entity)

#数据解析
print type(decode['list'])

#遍历列表数据
for i in decode['list']:

	reportdate = i['reportdate'];
	
	if reportdate.index('0331') >= 0:
		print '季度：' + reportdate[0:4] + '年' + '1季度'
	elif reportdate.index('0631') >= 0:
		print '季度：' + reportdate[0:4] + '年' + '2季度'
	elif reportdate.index('0931') >= 0:
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