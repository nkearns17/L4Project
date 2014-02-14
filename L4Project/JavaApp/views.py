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

def CYOtest(request):
	sys.path.append(os.getcwd()+'/static/programs/')
        template = loader.get_template('JavaApp/CYOtest.html')
	java_file = os.getcwd()+'/static/programs/HelloWorld.java'
	proc = subprocess.Popen(['javac ', java_file], stdout=subprocess.PIPE, shell=True)
	out = subprocess.check_call(['javac', java_file])
	jfile = os.getcwd()+'/static/programs/HelloWorld'
	cmd = ['java', jfile]
    	proc2 = subprocess.Popen(['java', jfile], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    	stdout,stderr = proc2.communicate()
	#cmd = ['java',  os.getcwd()+'/static/programs/HelloWorld']
        #out = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
	#stddata = proc.communicate()
	context = RequestContext(request, {})
	return HttpResponse(stdout)
	#java_file = '/static/programs/HelloWorld.java'
	#cmpfile = java_file + '.java'
	#cmd = 'javac ' + java_file

	# context = RequestContext(request, {})
	#proc = subprocess.Popen(cmd, shell=True)
	#try:
	#	out = subprocess.check_output(['java', '/static/programs/HelloWorld'])
	#	return HttpResponse(out)
	#except CalledProcessError as e:
    	#	return HttpResponse(e.returncode)

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

