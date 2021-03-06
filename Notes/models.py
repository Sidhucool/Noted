from django.db import models
from django.contrib.auth.models import User
from .current_user import get_current_user
from django.core.urlresolvers import reverse

# Create your models here.
class Note(models.Model):
	note_title = models.CharField(max_length=100)
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=get_current_user)
	note_content = models.TextField()
	note_remainder = models.DateTimeField()

	def __str__(self):
		return(self.note_title+'-'+self.note_content)

	def get_absolute_url(self):
		return reverse('Notes:index')		

class ListDo(models.Model):
	listdo_title = models.CharField(max_length=100)
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=get_current_user)
	listdo_remainder = models.DateTimeField()

	def __str__(self):
		return(self.listdo_title)

	def get_absolute_url(self):
		return reverse('Notes:index')	

class ListContent(models.Model):
	listdo=models.ForeignKey(ListDo,on_delete=models.CASCADE)
	content = models.CharField(max_length=1000)
	is_checked =models.BooleanField(default=False)

	def __str__(self):
		return(self.content)	

class Tag(models.Model):
	tag_title=models.CharField(max_length=100,unique=True)
	users = models.ManyToManyField(User)
	def __str__(self):
		return(self.tag_title)
	def get_absolute_url(self):
		return reverse('Notes:tag-view')	

class NoteTag(models.Model):
	tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
	note = models.ForeignKey(Note,on_delete=models.CASCADE)
	def __str__(self):
		return(self.tag.tag_title) 

class ListDoTag(models.Model):
	tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
	listdo = models.ForeignKey(ListDo,on_delete=models.CASCADE)
	def __str__(self):
		return(self.tag.tag_title)

	