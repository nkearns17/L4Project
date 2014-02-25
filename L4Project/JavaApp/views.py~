from django.http import HttpResponse
from django.template import RequestContext, loader
from JavaApp.models import Questions
from JavaApp.models import tutorial
from django.db import models
from django.http import HttpResponseRedirect
from django.utils import simplejson
from django.shortcuts import render_to_response
import subprocess
from subprocess import Popen, CalledProcessError, check_output, PIPE, STDOUT
import string
import urllib
import os, sys
from bs4 import BeautifulSoup
import re

def index(request):
	template = loader.get_template('JavaApp/Index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def home(request):
	template = loader.get_template('JavaApp/home.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def fib(request):
        template = loader.get_template('JavaApp/fib.html')
	questions = Questions.objects.filter(Qtype="FIB")
	javaWords = "month,first,third,tenth,year,System,out,println,for"
        context = RequestContext(request, {'questions':questions,'javaWords':javaWords})
        return HttpResponse(template.render(context))

def test5(request):
        template = loader.get_template('JavaApp/test5.html')
	questions = Questions.objects.filter(Qtype="FIB")
	javaWords = "continue, default, do, double, else, extends, false, final, finally, float, for, goto, if, implements, import, instanceof, int, interface, long, native, new, package, private, protected, public, return, short, static, super, switch, synchronized, this, throw, throws, transient, true, try, void, volatile, while, abstract, boolean, byte, case, catch, char, class, const, assert, break, enum, null, System, out, println, printf"
	listLength = len(javaWords)
        context = RequestContext(request, {'questions':questions,'javaWords':javaWords,'listLength':listLength})
        return HttpResponse(template.render(context))

def simpleFib(request):
        template = loader.get_template('JavaApp/simpleFib.html')
	questions = Questions.objects.filter(Qtype="FIB")
        context = RequestContext(request, {'questions':questions})
        return HttpResponse(template.render(context))

def about(request):
        template = loader.get_template('JavaApp/about.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def test(request):
        template = loader.get_template('JavaApp/test.html')
	questions = Questions.objects.filter(Qtype="MC")
        context = RequestContext(request, {'questions':questions})
        return HttpResponse(template.render(context))

def vtutorial(request):
        template = loader.get_template('JavaApp/vtutorials.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def tutorials(request):
        template = loader.get_template('JavaApp/tutorial.html')
	tuts = tutorial.objects.all()
        context = RequestContext(request, {'tuts':tuts})
        return HttpResponse(template.render(context))

def CYOtest(request):
        template = loader.get_template('JavaApp/CYOtest.html')
	questions = Questions.objects.filter(Qtype="CYO")
	context = RequestContext(request, {'questions':questions})
	return HttpResponse(template.render(context))

def runProg(request):
	if request.method == 'POST':
		text = request.POST['post']
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
	java_file = 'Test.java'
	f = open(java_file, 'w')
	f.write(text)
	proc = subprocess.Popen(['javac', java_file], stdout=subprocess.PIPE)
	#out = subprocess.check_call(['javac', java_file])
	proc2 = subprocess.Popen(['java','Test'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    	ans = proc2.communicate()
	return HttpResponse(ans)

#def multChoice(request):
#	template=loader.get_template('JavaApp/multChoice.html')
#	questions = Questions.objects.filter(Qtype="MC")
#	context = RequestContext(request, {'questions':questions})
#	return HttpResponse(template.render(context))

def multChoice2(request):
	template=loader.get_template('JavaApp/multChoice2.html')
	questions = Questions.objects.filter(Qtype="MC")
	context = RequestContext(request, {'questions':questions})
	return HttpResponse(template.render(context))

def validateAns(request, question, answer):
	dbquestion = Questions.objects.get(id=question)
	dbanswer = dbquestion.answer
	if answer == dbanswer:
		return HttpResponse("Your answer is correct!")
	else:
		return HttpResponse("Your answer is incorrect! Please try again.")

