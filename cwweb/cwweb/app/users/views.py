# -*- conding:utf-8 -*-
from django.shortcuts import render, render_to_response
# from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm
from .models import User_Profile


# Create your views here.


def index(request):
    return render(request, 'users/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, "users/Userlogin.html")

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                request.session['user'] = username
                return render(request, 'users/index.html')
            else:
                return render(request, 'users/Userlogin.html', {'error': '帐号密码错误'})
        else:
            return render(request, 'users/Userlogin.html', {'error': '帐号密码不合规'})


def Userlogout(request):
    # response = HttpResponse('logout')
    response = HttpResponseRedirect('/index/')
    logout(request)
    return response


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/Register.html')

    def post(self, request):
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data['username']
            FilterResult = User_Profile.objects.filter(username=username)
            if FilterResult:
                return render(request, 'users/Register.html', {'error': '用户名已存在'})
            email = registerform.cleaned_data['email']
            password = registerform.cleaned_data['password']
            user = User_Profile.objects.create_user(username=username
                                                    , email=email, password=password)
            user.save()
            respose = HttpResponseRedirect('/login/')
            return respose
        else:
            return render(request, 'users/Register.html', {'error': 'message is not valid'})
