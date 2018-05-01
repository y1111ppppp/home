# -*-coding:utf-8-*-
from django.conf.urls import include, url
# import xadmin
from . import views
from .views import LoginView, RegisterView

urlpatterns = [
    # url('admin/', admin.site.urls),
    # url('^xadmin/', xadmin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', views.Userlogout, name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
]
