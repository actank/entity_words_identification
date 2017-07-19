#coding:utf-8

import sys
sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf8')
import os
import re
import chardet
import jieba
import jieba.posseg as pseg
#数据清洗，得到较为规整的query

s_list = []
bow_list = []
def clean():
    output = open("./train.data", "w")
    with open("../data/prepare_data", "r") as f:
        for line in f:
            line = unicode(line.strip())
            
            #大小写归一化
            line = line.lower()
            
            #清除过短的query
            if len(line) <= 2:
                continue
            #清除爬虫爬宝贝id的query
            if re.match('[0-9]{18}', line) != None:
                continue
            #过滤全是英文的query
            eng_flag = True
            for i in line:
                if i >= u'\u4e00' and i <= u'\u9fa5':
                    eng_flag = False
                    break
            if eng_flag == True:
                continue
            #重新分词
            ll = jieba.cut(line)
            line = []
            for i in ll:
                if i == u"\u2006" or i == u" " or i == " ":
                    continue
                line.append(i)
            #过滤重复query
            if line in s_list:
                continue
            l = ",".join(line)
            s_list.append(line)
            output.write(l + "\n")
    output.close()
    return
def main():
    clean()
    return

if __name__ == "__main__":
    main()