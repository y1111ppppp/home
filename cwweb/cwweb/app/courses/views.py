# -*- conding:utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from .models import Orders
from .forms import OrderForm,TimeWidget
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
import datetime
import time

# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrdersView(View):
    def get(self, request, order_id):
        if str(order_id) == '0':
            return render(request, 'courses/Orders.html', {})
        order = Orders.objects.get(pk=order_id)
        return render(request, 'courses/Orders.html', {'order': order})
    def post(self,request):
        pass

@login_required
def order_edit(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order_id = request.POST.get('order_id_hidden', '0')
        num = request.POST.get('num', '0')
        company_simple = request.POST.get('company_simple', '')
        company = request.POST.get('company', '')
        money = request.POST.get('money', '0')
        if str(order_id) == '0':
            order = Orders.objects.create(num=num, company_simple=company_simple,
                                          company=company, money=money)
            order.save()
            return render(request, 'users/index.html',{'middle':'表单提交成功'})
        else:
            order = Orders.objects.get(pk=order_id)
            order.num = num
            order.company = company
            order.company_simple = company_simple
            order.money = money
            order.save()
            return render(request, 'users/index.html',{'middle':(order.company_simple,'已修改')})
    else:
        return render(request, 'users/index.html', {'middle': 'error'})

@method_decorator(login_required, name='dispatch')
class SelectView(View):
    def get(self,request):
        orders = Orders.objects.all()
        Sum = 0
        for i in orders:
            Sum += int(i.money)
        if request.GET.get('id', None):
            form = TimeWidget(instance=TimeWidget.objects.get(id=request.GET.get('id', None)))
        else:
            form = TimeWidget()
        return render(request, 'courses/orderperforman.html'
                      , {'orders': orders, 'sum': Sum})


    def post(self,request):

            start = request.POST.get('start_date','')
            # start = "2018/04/09"
            tmp = time.strptime(start, "%m/%d/%Y")
            y = tmp.tm_year
            m = tmp.tm_mon
            d = tmp.tm_mday
            start_time = datetime.datetime(int(y),int(m),int(d),0,0)
            end = request.POST.get('end_date','')
            # end = "2018/04/11"
            tmp = time.strptime(end, "%m/%d/%Y")
            y = tmp.tm_year
            m = tmp.tm_mon
            d = tmp.tm_mday
            end_time = datetime.datetime(int(y),int(m),int(d),0,0)
            orders = Orders.objects.filter(add_time__range=(start_time,end_time))
            Sum = 0
            for i in orders:
                Sum += int(i.money)
            return render(request,'courses/orderperforman.html',
                          {'orders': orders, 'sum': Sum,})




@login_required
def index(request):
    return render(request, 'courses/index.html')
@login_required
def DelOrder(request,order_id):
    order = Orders.objects.get(pk=order_id)
    order.delete()
    return render(request,'users/index.html',{'middle':'删除成功'})




