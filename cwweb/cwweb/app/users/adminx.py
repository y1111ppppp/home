# -*-coding:utf-8-*-
from __future__ import unicode_literals
__author__ = 'yxin'
__date__ = '18-3-31 上午9:41'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'


import xadmin
from xadmin import views
from .models import User_Profile,EmailVerfiCode,Banner


class EmailVerfiCodeadmin(object):
    list_display = ('code','email','send_type','send_time')
    list_filter = ('code', 'email', 'send_type', 'send_time')
    search_fields = ('code','email')

class Banneradmin(object):
    list_display = ('title', 'image', 'url', 'add_time', 'index')
    list_filter = ('title', 'image', 'url', 'add_time', 'index')
    search_fields = ('title', 'image', 'url', 'index')

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = '老妈的财务管理后台'
    site_footer = '个人练习'
    menu_style = 'accordion'

#xadmin.site.register(User_Profile)
xadmin.site.register(EmailVerfiCode,EmailVerfiCodeadmin)
xadmin.site.register(Banner,Banneradmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)