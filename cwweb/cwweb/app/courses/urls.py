# -*-coding:utf-8-*-
from django.conf.urls import include, url
# import xadmin
from . import views
from .views import OrdersView , SelectView

urlpatterns = [
    url(r'^submitorder/(?P<order_id>[0-9]+)$', OrdersView.as_view(), name='sumbitorder'),
    url(r'^selectorder/$', SelectView.as_view(), name='selectorder'),
    url(r'^order_edit/$', views.order_edit, name='order_edit_action'),
    url(r'^delorder/(?P<order_id>[0-9]+)$', views.DelOrder, name='delorder'),
]
