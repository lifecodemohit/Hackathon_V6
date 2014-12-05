from django.db import models

# Create your models here.

class Question(models.Model) :
	name = models.CharField(max_length=200)
	heading = models.TextField()
	qText = models.TextField()
	pub_date = models.DateTimeField(auto_now=True)
	votes = models.IntegerField(default = 0)
	extra = models.TextField()
	extra1 = models.TextField()
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.heading

class Comments(models.Model) :
	qComment = models.ForeignKey(Question)
	cName = models.CharField(max_length=200)
	cText = models.TextField()
	cpub_date = models.DateTimeField(auto_now=True)
	cvotes = models.IntegerField(default = 0)
	cextra = models.TextField()
	cextra1 = models.TextField()
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.cName


class Category(models.Model) :
	qCat = models.ForeignKey(Question)
	qText = models.CharField(max_length=200)
	extra = models.TextField()
	extra1 = models.TextField()

