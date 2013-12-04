from django.conf.urls import patterns,url

from JavaApp import views

urlpatterns = patterns('',
	url(r'^index', views.index, name='index'),
	url(r'^fib', views.fib, name='fib'),
	url(r'^$', views.home, name='home'),
	url(r'^test', views.test, name='test'),
	url(r'^about', views.about, name='about'),
)
