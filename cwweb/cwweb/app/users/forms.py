# -*-coding:utf-8-*-
__author__ = 'yxin'
__date__ = '18-4-8 下午10:04'
__product__ = 'PyCharm'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=20)
    password = forms.CharField(required=True,min_length=6)
    #email = forms.EmailField()

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,max_length=20)
    email = forms.EmailField(required=True,)
    password = forms.CharField(required=True,min_length=6)
