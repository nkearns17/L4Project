from django.http import HttpResponse
from django.template import RequestContext, loader
from JavaApp.models import Questions
from JavaApp.models import tutorial
from JavaApp.models import cyoQuestions
from JavaApp.models import videoTutorials
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
	questions = Questions.objects.filter(Qtype="FIB").order_by('?')
	javaWords = "continue, println, printf, default, do, double, else, extends, false, final, finally, float, for, goto, if, implements, int, import, instanceof, interface, long, native, new, package, private, protected, public, return, short, static, super, switch, synchronized, this, throw, throws, transient, true, try, void, volatile, while, abstract, boolean, byte, case, catch, char, const, assert, break, enum, null, System, out"
        context = RequestContext(request, {'questions':questions,'javaWords':javaWords})
        return HttpResponse(template.render(context))

def test5(request):
        template = loader.get_template('JavaApp/test5.html')
	questions = Questions.objects.filter(Qtype="FIB")
	javaWords = "continue, default, do, double, else, extends, false, final, finally, float, for, goto, if, implements, import, instanceof, interface, long, native, new, package, private, protected, public, return, short, static, super, switch, synchronized, this, throw, throws, transient, true, try, void, volatile, while, abstract, boolean, byte, case, catch, char, const, assert, break, enum, null, System, out, println, printf"
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
	vTuts = videoTutorials.objects.all()
        context = RequestContext(request, {'vTuts':vTuts})
        return HttpResponse(template.render(context))

def tutorials(request):
        template = loader.get_template('JavaApp/tutorial.html')
	tuts = tutorial.objects.all()
	nameList = tutorial.objects.all().values_list('tutName')
        context = RequestContext(request, {'tuts':tuts, 'nameList':nameList})
        return HttpResponse(template.render(context))

def CYOtest(request):
        template = loader.get_template('JavaApp/CYOtest.html')
	questions = cyoQuestions.objects.filter(qType="CYO")
	context = RequestContext(request, {'questions':questions})
	return HttpResponse(template.render(context))

def Fbc(request):
        template = loader.get_template('JavaApp/Fbc.html')
	questions = cyoQuestions.objects.filter(qType="FBC")
	context = RequestContext(request, {'questions':questions})
	return HttpResponse(template.render(context))


def runProg(request, question):
	# gets the question from the db
	dbquestion = cyoQuestions.objects.get(id=question)
	# get the entered code
	if request.method == 'POST':
		text = request.POST['post']
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
	# get the java files - code and junit test
	java_file = os.getcwd()+'/static/cyoTests/cTest.java'
	test_file ='codeTest'+question+'.java'
	# write to file
	f = open(java_file, 'w')
	f.write(text)
	# paths for the .jar files
	ham = os.getcwd()+'/hamcrest-core-1.3.jar'
	jjar = os.getcwd()+'/junit.jar'
	jar_path = ':'+ham+":"+jjar
	# set the classpath to include both .jar's
	os.environ['CLASSPATH'] = jar_path
	# compile both the users code and the junit test
	proc = subprocess.Popen(['javac','-cp',os.environ['CLASSPATH'], java_file], stdout=subprocess.PIPE)
	# change to cyoTests directory
	os.chdir('./static/cyoTests/')
	proc2 = subprocess.Popen(['javac','-cp',os.environ['CLASSPATH'], test_file], stdout=subprocess.PIPE)
	#out = subprocess.check_call(['javac', java_file])
	jTest = 'codeTest'+question
	# run the junit test
	proc3 = subprocess.Popen(['java', '-cp',os.environ['CLASSPATH'],'org.junit.runner.JUnitCore',jTest], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    	ans = proc3.communicate()
	os.chdir('../../')
	return HttpResponse(ans)

#def multChoice(request):
#	template=loader.get_template('JavaApp/multChoice.html')
#	questions = Questions.objects.filter(Qtype="MC")
#	context = RequestContext(request, {'questions':questions})
#	return HttpResponse(template.render(context))

def multChoice2(request):
	template=loader.get_template('JavaApp/multChoice2.html')
	questions = Questions.objects.filter(Qtype="MC").order_by('?')
	context = RequestContext(request, {'questions':questions})
	return HttpResponse(template.render(context))

def validateAns(request, question, answer):
	dbquestion = Questions.objects.get(id=question)
	dbanswer = dbquestion.answer
	if answer == dbanswer:
		return HttpResponse("Your answer is correct!")
	else:
		return HttpResponse("Your answer is incorrect! Please try again.")

