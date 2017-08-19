# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

def getHeaders():
	reqHeader = {
		'Host': 'xueqiu.com',
		'Cookie': '66c2d36007ff06e2686dc5555681b887; u=701502715757765; s=g413wj53q7; Hm_lvt_1db88642e346389874251b5a1eded6e3=1502715758,1502715772,1502715919,1503102157; __utma=1.484125305.1503102157.1503102157.1503102157.1; __utmz=1.1503102157.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAFPxfG0WqwgA69CctG0k+/Ae9blI; xq_a_token=dc17410b1142590a3bab370bbfe3c1f6546832e1; xq_r_token=257f33a651bc541e6315602eb995d5703d7d0f3a'
	}
	return reqHeader

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)

print sys.argv[1]