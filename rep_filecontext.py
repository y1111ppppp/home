#!/usr/bin/python
#-*- conding:utf-8 -*-
def rep_test(file):
    import os,re
    aaa = '我要做替换测试'
    bbb = '测试成功啦'
    with open(file,'r') as fp,open('{name}_bak.txt'.format(name = file),'w+') as fq:
        for line in fp:
            fq.write(re.sub(aaa,bbb,line))
    os.remove(file)
    os.rename('{name}_bak.txt'.format(name = file),file)
if __name__ == '__main__':
    file = 'E:\\python\\re_test.txt'
    rep_test(file)
