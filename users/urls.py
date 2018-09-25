"""为应用程序users定义URL模式"""
#from django.conf.urls import url
from django.urls import path

#from django.contrib.auth.views import login  Dajango2.1已经不用这种写法
from django.contrib.auth.views import LoginView

from . import views

#命名空间
app_name = "users"

urlpatterns = [
    # 登录页面
    #url(r'^login/$', login, {'template_name': 'users/login.html'},name='login'),
    #path('login/', login, {'template_name': 'users/login.html'},name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    #注销
    path('logout/', views.logout_view, name='logout'),

    # 注册页面
    #url(r'^register/$', views.register, name='register'),
    path('register/', views.register, name='register'),
]