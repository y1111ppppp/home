from __future__ import unicode_literals
from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User_Profile(AbstractUser):
    nick_name = models.CharField(max_length=50,default=u'',verbose_name=u'昵称')
    birth = models.DateField(verbose_name='生日',null=True,blank=True)
    gender = models.CharField(max_length=5,choices=((u'男','male'),
                              (u'女','female')),verbose_name=u'性别')
    address = models.CharField(max_length=100,verbose_name='地址',default=u'')
    mobile = models.CharField(max_length=11,verbose_name=u'电话',null=True,blank=True)
    avatar = models.ImageField(max_length=100,upload_to=u'avatar/%Y/%m',
                               default=u'avatar/default.png',verbose_name=u'用户头像')

    class Meta:
        verbose_name=u'用户信息表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

class EmailVerfiCode(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.EmailField(max_length=50,verbose_name=u'邮箱地址')
    send_type = models.CharField(max_length=10,choices=(('register',u'注册'),
                                                        ('forget',u'忘记密码')))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{0}---({1})'.format(self.code,self.email)

class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'标题')
    image=models.ImageField(max_length=100,
                            verbose_name=u'图片地址',upload_to='banner/%Y/%M')
    url=models.CharField(max_length=200,verbose_name=u'跳转地址')
    add_time = models.DateTimeField(default=datetime.now)
    index = models.IntegerField(default=100,verbose_name=u'排列顺序')

    class Meta:
        verbose_name=u'轮波图'
        verbose_name_plural=verbose_name
