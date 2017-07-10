#coding:utf-8

import sys
import os
import re

s_list = []
def main():

    with open("../data/prepare_data", "r") as f:
        for line in f:
            line = line.strip()
            #清除单个英文字符的query
            if len(line) == 1:
                continue
            #清除爬虫爬宝贝id的query
            if re.match('[0-9]{18}', line) != None:
                continue
            #过滤重复query
            if line not in s_list:
                s_list.append(line)
                print line
    return

if __name__ == "__main__":
    main()
