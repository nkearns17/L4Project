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
	javaWords = "month,first,third,tenth,year,System,out,println,for"
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

def compile_java(java_file):
	subprocess.check_call(['javac', java_file])

def execute_java(java_file):
	java_class,ext = os.path.splitext(java_file)
	cmd = ['java', java_class]
	proc = subprocess.check_output(cmd)
	return HttpResponse(proc)

def CYOtest(request):
	sys.path.append(os.getcwd()+'/static/programs/')
	javapath = '/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.51.x86_64/jre/bin/java'
	os.environ['CLASSPATH'] = javapath
        template = loader.get_template('JavaApp/CYOtest.html')
	java_file = os.getcwd()+'/static/programs/HelloWorld.java'
	proc = subprocess.Popen(['javac', java_file], stdout=subprocess.PIPE)
	out = subprocess.check_call(['javac', java_file])
	jfile = os.getcwd()+'/static/programs/HelloWorld'
    	proc2 = subprocess.Popen(['java','-cp','./static/programs/', 'HelloWorld'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    	ans = proc2.communicate()
	context = RequestContext(request, {})
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

def validateFIB(request, question, answer):
	dbquestion = Questions.objects.get(id=question)
	dbanswer = dbanswer.answer
	if answer == dbanswer:
		return HttpResponse("Your answer is correct!")
	else:
		return HttpResponse("Your answer is incorrect!")

