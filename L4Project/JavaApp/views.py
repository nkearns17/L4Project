from django.http import HttpResponse
from django.template import RequestContext, loader
from JavaApp.models import Questions
from JavaApp.models import tutorial
from django.db import models
from django.http import HttpResponseRedirect
from django.utils import simplejson
from django.shortcuts import render_to_response
import subprocess
from subprocess import Popen, CalledProcessError, check_output, PIPE
import string

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

def tutorial(request):
        template = loader.get_template('JavaApp/tutorial.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def CYOtest(request):
        template = loader.get_template('JavaApp/CYOtest.html')
	java_file = '/users/level4/0902059k/Level4/HelloWorldApp'
	cmpfile = java_file + '.java'
	cmd = 'javac ' + cmpfile

	# context = RequestContext(request, {})
	#proc = subprocess.Popen(cmd, shell=True)
	try:
		out = subprocess.check_output(["java",java_file])
		return HttpResponse(out)
	except CalledProcessError as e:
    		return HttpResponse(e.returncode)

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
		return HttpResponse("Your answer is incorrect!")

def validateFIB(request, question, answer):
	dbquestion = Questions.objects.get(id=question)
	dbanswer = dbanswer.answer
	if answer == dbanswer:
		return HttpResponse("Your answer is correct!")
	else:
		return HttpResponse("Your answer is incorrect!")

