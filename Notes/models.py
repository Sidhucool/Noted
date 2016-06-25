from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
	note_title = models.CharField(max_length=100)
	user = models.ForeignKey(User)
	note_content = models.TextField()
	note_remainder = models.DateTimeField()

	def __str__(self):
		return(self.note_title+'-'+self.note_content)

class DoList(models.Model):
	doList_title = models.CharField(max_length=100)
	doList_content = models.TextField()
	user = models.ForeignKey(User)
	doList_remainder = models.DateTimeField()
	Is_doList_checked =models.BooleanField(default=False)

	def __str__(self):
		return(self.doList_title+'-'+self.doList_content)

class Tag(models.Model):
	tag_title=models.CharField(max_length=100,unique=True)
	notes=models.ManyToManyField(Note)
	dolists=models.ManyToManyField(DoList)

	def __str__(self):
		return(self.tag_title)
				