#coding:utf-8

import sys
sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf8')
import os
import re
import chardet
import jieba
import json
import urllib2
import string

def main():
	ret = urllib2.urlopen("http://wormhole.inf.lehe.com/se_slave1/ProductCore/SearchV03?fl=GoodsId&wt=json&indent=true&facet=true&facet.field=BrandEnName")
	bd = json.loads(ret.read())
	tmp = bd['facet_counts']['facet_fields']['BrandEnName']
	brand_list = []

	delset = string.punctuation
	with open("../data/brand_dict", "w") as f:
		for i in range(len(tmp)):
			if i % 2 == 1:
				continue
			l = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),tmp[i])
			f.write(l + "\n")

	return

if __name__ == "__main__":
	main()
