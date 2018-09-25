"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# 书中的内容和实际的内容有些出入，以下是书中内容：
# 新版Django简化了URL路由写法
# from django.conf.urls import include, url
# from django.contrib import admin
# 
# from django.conf.urls import include, url
# from django.contrib import admin
#
# urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
# ]

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^users/', include('users.urls', namespace='users')),
    path("users/", include("users.urls")),
    path("", include("learning_logs.urls")),

]
