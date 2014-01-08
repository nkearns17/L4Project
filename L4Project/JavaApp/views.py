from django.http import HttpResponse
from django.template import RequestContext, loader
from JavaApp.models import Questions
from django.db import models
from django.http import HttpResponseRedirect
from django.utils import simplejson
from django.shortcuts import render_to_response

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
        context = RequestContext(request, {'questions':questions})
        return HttpResponse(template.render(context))

#def test(request):
#        template = loader.get_template('JavaApp/test.html')
#	questions = Questions.objects.filter(Qtype="FIB")
#	javaWords = ["month","first","third","tenth","year"]
#	listLength = len(javaWords)
#        context = RequestContext(request, {'questions':questions,'javaWords':javaWords,'listLength':listLength})
#        return HttpResponse(template.render(context))

def test2(request):
        template = loader.get_template('JavaApp/test2.html')
	questions = Questions.objects.filter(Qtype="FIB")
	javaWords = ["month","first","third","tenth","year"]
	listLength = len(javaWords)
        context = RequestContext(request, {'questions':questions,'javaWords':javaWords,'listLength':listLength})
        return HttpResponse(template.render(context))

def about(request):
        template = loader.get_template('JavaApp/about.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def mctest(request):
	template=loader.get_template('JavaApp/mctest.html')
	questions = Questions.objects.filter(Qtype="MC")
	context = RequestContext(request, {'questions':questions})
	return HttpResponse(template.render(context))

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
	if answer==dbanswer:
		return HttpResponse("Your answer is correct!")
	else:
		return HttpResponse("Your answer is incorrect!")

def validateFIB(request, keyword, userWord):
	if keyword == userWord:
		return HttpResponse("Your answer is correct!")
	else:
		return HttpResponse("Your answer is incorrect!")
