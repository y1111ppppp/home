# -*-coding:utf-8-*-
__author__ = 'yxin'
__date__ = '18-4-8 下午10:04'
__product__ = 'PyCharm'


from django.db import models



from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


# Bootstrap 3

class TimeWidget(forms.Form):
    # start_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    # end_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    start_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    end_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    # time = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))


class OrderForm(forms.Form):
    num = forms.IntegerField(required=True)
    company_simple = forms.CharField(max_length=20, required=True)
    company = forms.CharField(max_length=50, required=True)
    money = forms.IntegerField(required=True)
    # money_type = forms.CharField(max_length=3,default=u'人民币',verbose_name=u'币种')
    # add_time = forms.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
