
"""定义learning_logs的URL模式"""
# from django.conf.urls import url
# from . import views


# urlpatterns = [
#     # 主页
#     url(r'^$', views.index, name='index'),

# ]

from django.urls import path

from . import views

#命名空间
app_name = "learning_logs"

urlpatterns = [
    #主页
    path("",views.index,name="index"),

    # 显示所有的主题
    #url(r'^topics/$', views.topics, name='topics'),
    path("topics/", views.topics, name='topics'),

    # 特定主题的详细页面
    path("topics/<int:topic_id>/", views.topic, name='topic'),
    #url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用于添加新主题的网页
    path("new_topic/", views.new_topic, name='new_topic'),
    #url(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    # 用于添加新条目的页面
    #url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    path("new_entry/<int:topic_id>/", views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    #url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry,name='edit_entry'),
    
]