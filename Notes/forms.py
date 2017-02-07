from django.contrib.auth.models import User
from django import forms
from .models import Note,ListDo,ListContent,Tag,NoteTag,ListDoTag
from .current_user import get_current_user
from django.forms.models import inlineformset_factory
class UserForm(forms.ModelForm):
	password =forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields =['username','password']

class NoteForm(forms.ModelForm):

	class Meta:
		model = Note
		fields =['note_title','note_content','note_remainder']
class ListDoForm(forms.ModelForm):

	class Meta:
		model = ListDo
		fields =['listdo_title','listdo_remainder']

class ListContentForm(forms.ModelForm):

	class Meta:
		model = ListContent
		fields =['content','is_checked']
	
ListContentFormSet = inlineformset_factory(ListDo, ListContent,exclude=['listdo',],)

class TagForm(forms.Form):
	tag = forms.CharField(
	label='Tag title',
	required=True,
	widget=forms.TextInput(attrs={'size': 32})
	)

	def clean_tag(self):
          data = self.cleaned_data['tag']
          if Tag.objects.filter(tag_title=data,users=get_current_user()):
              raise forms.ValidationError("Tag exists")
          return data

class NoteTagForm(forms.Form):

	def __init__(self,*args,**kwargs):

		self.form_pk=kwargs.pop('note_id')
		super(NoteTagForm,self).__init__(*args,**kwargs)

	tag = forms.CharField(
	label='Tag title',
	required=True,
	widget=forms.TextInput(attrs={'size': 32})
	)

	def clean_tag(self):
          data = self.cleaned_data['tag']
          note=Note.objects.get(id=self.form_pk)
          if NoteTag.objects.filter(tag__tag_title=data,note=note):
              raise forms.ValidationError("Tag exists for this note")
          return data

class ListDoTagForm(forms.Form):

	def __init__(self,*args,**kwargs):

		self.form_pk=kwargs.pop('listdo_id')
		super(ListDoTagForm,self).__init__(*args,**kwargs)

	tag = forms.CharField(
	label='Tag title',
	required=True,
	widget=forms.TextInput(attrs={'size': 32})
	)

	def clean_tag(self):
          data = self.cleaned_data['tag']
          listdo=ListDo.objects.get(id=self.form_pk)
          if ListDoTag.objects.filter(tag__tag_title=data,listdo=listdo):
              raise forms.ValidationError("Tag exists for this to-dolist")
          return data         