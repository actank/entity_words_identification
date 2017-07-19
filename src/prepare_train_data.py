#coding:utf-8

import sys
sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf8')
import os
import re
import chardet
import jieba
import jieba.posseg


def main():
	output = open("crf_train.data", "w")
	cnt = 0
	with open("./tagged.data", "r") as f:
		for line in f:
			line = line.strip().split(",")
			flag = False
			for i in line:
				if re.search("[PBMSTLE]-", i) == None:
					flag = True
					break
			if flag == True:
				continue
			for l in line:
				output.write(l + "\n")
			output.write("\n")
			
	output.close()
	return

if __name__ == "__main__":
	main()
