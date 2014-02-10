from django.conf.urls import patterns,url

from JavaApp import views

urlpatterns = patterns('',
	url(r'^index', views.index, name='index'),
	url(r'^fib', views.fib, name='fib'),
	url(r'^$', views.home, name='home'),
	url(r'^about', views.about, name='about'),
	url(r'^validate_answer/(?P<question>\w+)/(?P<answer>\d+\.\d+)','JavaApp.views.validateAns'),
	url(r'^validate_answer/(?P<question>\w+)/(?P<answer>\w+)', 'JavaApp.views.validateAns'),
	#url(r'^multChoice', views.multChoice),
	url(r'^validate_fib/(?P<question>\w+)/(?P<answer>\d+\.\d+)','JavaApp.views.validateFIB'),
	url(r'^validate_fib/(?P<question>\w+)/(?P<answer>\w+)', 'JavaApp.views.validateFIB'),
	url(r'^multChoice2', views.multChoice2),
	url(r'^test5', views.test5,name='test5'),
	url(r'^simpleFib', views.simpleFib),
	url(r'^test', views.test,name='test'),
	url(r'^vtutorial', views.vtutorial),
	url(r'^tutorials', views.tutorials),
	url(r'^CYOtest', views.CYOtest),
)
