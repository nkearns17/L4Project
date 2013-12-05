# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from JavaApp.models import MCQuestions


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
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def test(request):
        template = loader.get_template('JavaApp/test.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def about(request):
        template = loader.get_template('JavaApp/about.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def mctest(request):
	template=loader.get_template('JavaApp/mctest.html')
	questions = MCQuestions.objects.all()
	context = RequestContext(request, {'questions':questions})
	return HttpResponse(template.render(context))

def validateAns(request, question, answer):
	dbquestion = MCQuestions.objects.get(id=question)
	dbanswer = dbquestion.answer
	if (answer == dbanswer):
		return HttpResponse("Your answer is correct!")
	else:
		return HttpResponse("Your answer is incorrect!")
