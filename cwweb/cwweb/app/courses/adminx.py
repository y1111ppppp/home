# -*-coding:utf-8-*-

import xadmin
from .models import Course,Lesson,Video,CourseResource,Orders
__author__ = 'yxin'
__date__ = '18-3-31 上午10:30'
__product__ = 'PyCharm'
__filename__ = 'adminx' + '.py'


class Courseadmin(object):
    list_display = ('name', 'desc', 'detail', 'degree', 'learn_duration', 'student_num','favorites_num',
                    'image','click_num','add_time')
    list_filter = ('name','desc','detail','degree','learn_duration','student_num','favorites_num',
                    'image','click_num','add_time')
    search_fields = ('name','desc','detail','degree','learn_duration','student_num','favorites_num',
                    'image','click_num')

class Lessonadmin(object):
    list_display = ('course', 'name', 'add_time')
    list_filter = ('course__name', 'name', 'add_time')
    search_fields = ('Course__name', 'name')

class Videoadmin(object):
    list_display = ('lesson', 'name', 'add_time')
    list_filter = ('lesson__name', 'name', 'add_time')
    search_fields = ('lesson__name', 'name')

class CourseResourceadmin(object):
    list_display = ('course', 'name', 'add_time','download')
    list_filter = ('course__name', 'name', 'add_time','download')
    search_fields = ('course__name', 'name','download')

class Ordersadmin(object):
    list_display = ('num','company_simple','company','money','money_type','add_time')
    list_filter = ('num','company_simple','company','money','add_time')
    search_fields = ('num','company_simple','company','money')

xadmin.site.register(Course,Courseadmin)
xadmin.site.register(Lesson,Lessonadmin)
xadmin.site.register(Video,Videoadmin)
xadmin.site.register(CourseResource,CourseResourceadmin)
xadmin.site.register(Orders,Ordersadmin)