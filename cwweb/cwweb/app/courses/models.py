from __future__ import unicode_literals
from django.db import models
# from datetime import date
from datetime import datetime
# from django.utils.timezone import now



class Orders(models.Model):
    num = models.IntegerField(default=0,verbose_name=u'凭证号')
    company_simple = models.CharField(max_length=30,verbose_name=u'公司简称')
    company = models.CharField(max_length=50,verbose_name=u'公司名称')
    money = models.IntegerField(default=0,verbose_name=u'金额')
    money_type = models.CharField(max_length=3,default=u'人民币',verbose_name=u'币种')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    add_date = models.DateTimeField(default=datetime.today,verbose_name=u'添加日期')
    class Meta:
        verbose_name = u'财务凭证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company
