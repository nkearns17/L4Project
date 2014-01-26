from django.db import models

class Questions(models.Model):
	Qtype = models.CharField(max_length=100)
	topic = models.CharField(max_length=100)
	question = models.TextField(max_length=1000)
	posAns1 = models.CharField(max_length=300)
	posAns2 = models.CharField(max_length=300)
	posAns3 = models.CharField(max_length=300)
	posAns4 = models.CharField(max_length=300)
	answer = models.CharField(max_length=300)
	level = models.CharField(max_length=100)

	def __unicode__(self):
       		return self.question
