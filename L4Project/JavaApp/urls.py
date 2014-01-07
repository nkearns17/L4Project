from django.conf.urls import patterns,url

from JavaApp import views

urlpatterns = patterns('',
	url(r'^index', views.index, name='index'),
	url(r'^fib', views.fib, name='fib'),
	url(r'^$', views.home, name='home'),
	#url(r'^test', views.test, name='test'),
	url(r'^about', views.about, name='about'),
	url(r'^mctest', views.mctest),
	url(r'^validate_answer/(?P<question>\w+)/(?P<answer>\d+\.\d+)','JavaApp.views.validateAns'),
	url(r'^validate_answer/(?P<question>\w+)/(?P<answer>\w+)', 'JavaApp.views.validateAns'),
	url(r'^multChoice', views.multChoice),
	url(r'^test2', views.test2, name='test2'),
)
