'''定义learning_logs的URL模式'''

from django.conf.urls import url, include
from . import views

urlpatterns = [
	# 主页
	url(r'^$', views.index, name='index'),

	# 主题
	url(r'^topics/$', views.topics, name='topics'),

	# 特定主题的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]