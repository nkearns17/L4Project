from django.db import models

class MCQuestions(models.Model):
	question = models.CharField(max_length=1000)
	posAns1 = models.CharField(max_length=300)
	posAns2 = models.CharField(max_length=300)
	posAns3 = models.CharField(max_length=300)
	answer = models.CharField(max_length=300)
	level = models.CharField(max_length=100)

	def __unicode__(self):
       		return self.question
