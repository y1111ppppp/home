#!/usr/bin/python
#-*-conding: utf-8 -*-
#删除30天以前的日志
def delfile(filename):
    import time
    import datetime
    import os
    filenames = os.listdir(filename)
    for i in filenames:
        if i[-3:] == 'log':
            file_date = os.path.getmtime(filename + i)
            now = time.time()
            time1 = (now - file_date)/60/60/24
            print(time1)
            if time1 >= 30:
                try:
                    os.remove(filename + i)
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    filename = '/tmp/'
    delfile(filename)
