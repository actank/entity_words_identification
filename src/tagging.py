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

product_dict = {}
brand_dict = {}
location_dict = {}
attr_dict = {}

def read_product_dict():
    with open("../data/ikdic/product_ext.dic", "r") as f:
        for line in f:
            line = line.strip()
            product_dict[line] = 1
    return
def read_brand_dict():
    with open("../data/ikdic/brand_ext.dic", "r") as f:
        for line in f:
            line = line.strip()
            brand_dict[line.lower()] = 1
    return
def read_location_dict():
    with open("../data/ikdic/location_ext.dic", "r") as f:
        for line in f:
            line = line.strip()
            location_dict[line] = 1
    return

def read_attr_dict():
    with open("../data/ikdic/style_ext.dic", "r") as f:
        for line in f:
            line = line.strip()
            attr_dict[line] = 1
    return

def tagging():
    output = open("./tagged.data", "w")
    with open("./train.data", "r") as f:
        for line in f:
            line = line.strip()
            ll = line.split(",")
            for i in range(len(ll)):
                term = ll[i]
                tagged_term = []
                if product_dict.has_key(term):
                    term = term.decode('utf-8')
                    for j in range(len(term)):
                        if j == 0:
                            tagged_term.append(term[j] + " B-product")
                        else:
                            tagged_term.append(term[j] + " I-product")
                    ll[i] = ",".join(tagged_term)
                if brand_dict.has_key(term):
                    term = term.decode('utf-8')
                    for j in range(len(term)):
                        if j == 0:
                            tagged_term.append(term[j] + " B-brand")
                        else:
                            tagged_term.append(term[j] + " I-brand")
                    ll[i] = ",".join(tagged_term)
                if location_dict.has_key(term):
                    term = term.decode('utf-8')
                    for j in range(len(term)):
                        if j == 0:
                            tagged_term.append(term[j] + " B-location")
                        else:
                            tagged_term.append(term[j] + " I-location")
                    ll[i] = ",".join(tagged_term)
                if attr_dict.has_key(term):
                    term = term.decode('utf-8')
                    for j in range(len(term)):
                        if j == 0:
                            tagged_term.append(term[j] + " B-attr")
                        else:
                            tagged_term.append(term[j] + " I-attr")
                    ll[i] = ",".join(tagged_term)
            output.write(",".join(ll) + "\n")
    output.close()

    return


def main():
    read_product_dict()
    read_brand_dict()
    read_location_dict()
    read_attr_dict()
    tagging()
    return

if __name__ == "__main__":
    main()
