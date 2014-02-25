from django.db import models

class Questions(models.Model):
	Qtype = models.CharField(max_length=100)
	topic = models.CharField(blank=True, max_length=100)
	question = models.TextField(max_length=1000)
	posAns1 = models.CharField(blank=True, max_length=300)
	posAns2 = models.CharField(blank=True, max_length=300)
	posAns3 = models.CharField(blank=True, max_length=300)
	posAns4 = models.CharField(blank=True, max_length=300)
	answer = models.CharField(blank=True, max_length=300)
	level = models.CharField(blank=True, max_length=300)

	def __unicode__(self):
       		return self.question

class tutorial(models.Model):
	tutTopic = models.CharField(max_length=100)
	tutName = models.CharField(max_length=100)	
	tutFile = models.FileField(upload_to='tutorials', max_length=500)

	def __unicode__(self):
       		return self.tutName
