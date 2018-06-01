#!/usr/bin/python
#-*-conding: utf-8 -*-
#统计访问量
def statistical_access(filename):
    with open(filename,'r') as fp:
        aaa = {}
        for line in fp.readlines():
            if line.split()[0] in aaa:
                aaa[line.split()[0]] += 1
            else:
                aaa[line.split()[0]] = 1
        print(aaa)
    bbb = sorted(aaa.items(),key = lambda x:x[1],reverse = True)
    for i in range(10):
        print(bbb[i])

