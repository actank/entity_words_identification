#coding:utf-8

import sys
sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf8')
import os
import re
import jieba
import jieba.posseg as pseg
#数据清洗，得到较为规整的query

s_list = []
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
            #重新分词
            ll = jieba.cut(line)
            line = ""
            for i in ll:
                if i == u"\u2006" or i == u" " or i == " ":
                    continue
                line = line + i + "/"
            line = line[:len(line)-2]
            if line[len(line) - 1] == "/":
                line = line[:len(line) - 2]
            #line = "/".join(line.split(" "))
            #line = "/".join(line.split(u'\u2006'))
            #再次过滤长度小于3的query
            if len(line.split("/")) <= 3:
                continue
            #过滤长度大于6的query
            if len(line.split("/")) >6 : 
                continue

            #过滤重复query
            if line in s_list:
                continue
            s_list.append(line)
            output.write(line + "\n")
    output.close()
    return
def tagging():
    with open("./train.data", "r") as f:
        for line in f:
            line = line.strip()
            line = line.replace("/", " ")
            seg = pseg.cut(line)
            for word, flag in seg:
                if flag.strip() == "x":
                    continue
                print "%s\t%s" % (word, flag)
        
    return
def main():
    #clean()
    tagging()
    return

if __name__ == "__main__":
    main()
