from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View,TemplateView,ListView
from .models import Note,ListDo,ListContent,Tag
from django.core.urlresolvers import reverse_lazy
from .forms import *
from django.forms.models import inlineformset_factory
from .current_user import get_current_user
# Create your views here.
@login_required(login_url='/notes/login/')
def index(request):
	#current_user=request.user
	all_notes = Note.objects.filter(user=request.user)
	all_listdos=ListDo.objects.filter(user=request.user)
	#template = loader.get_template('Notes/index.html')
	context = {'all_notes':all_notes,'user':request.user,'all_listdos':all_listdos}
	return render (request,'Notes/index.html',context)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/notes/main_page')

def main_page(request):
	return render(request,'Notes/main_page.html')	

class UserFormView(View):
	form_class = UserForm
	template_name ='Notes/registration_form.html'	

	#display blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	#process form Data	
	def post (self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned(Normalized) data

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credential are Correct
			user =authenticate(username=username,password=password)

			if user is not None:

				if user.is_active:
					login(request,user)
					return redirect('Notes:index')

		return render(request,self.template_name,{'form':form})	

class NoteCreate(CreateView):
	form_class = NoteForm
	template_name ='Notes/note_form.html'		
	#display blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	#process form Data	
	def post (self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			note = form.save(commit=False)

			#cleaned(Normalized) data

			note_title = form.cleaned_data['note_title']
			note_content = form.cleaned_data['note_content']
			note_remainder = form.cleaned_data['note_remainder']
			note.save()

			return redirect('Notes:index')

		return render(request,self.template_name,{'form':form})		
    	
class NoteUpdate(UpdateView):
	model = Note
	fields = ['note_title','note_content','note_remainder']

class NoteDelete(DeleteView):
	model = Note
	success_url = reverse_lazy('Notes:index')

class ListDoCreate(TemplateView):
	form_class = ListDoForm
	template_name ='Notes/listdo_create.html'		
	#display blank form
	def get(self,request):
		form = self.form_class(None)
		EventDayFormSet = inlineformset_factory (ListDo,ListContent,fields=('content','is_checked',))
		formset = EventDayFormSet()
		context = {'form': form, 'formset': formset}
		return render(request,self.template_name,context)

	#process form Data	
	def post (self,request):
		form = self.form_class(request.POST)
		EventDayFormSet = inlineformset_factory(ListDo, ListContent,fields=('content','is_checked',))
		formset = EventDayFormSet(request.POST)
		if form.is_valid():
			listdo = form.save(commit=False)

			#cleaned(Normalized) data

			listdo_title = form.cleaned_data['listdo_title']
			listdo_remainder = form.cleaned_data['listdo_remainder']
			listdo.save()
			listcontents = formset.save(commit=False)
			for listcontent in listcontents:
				listcontent.listdo = listdo
				listcontent.save()
			return redirect('Notes:index')
		context = {'form': form, 'formset': formset}	
		return render(request,self.template_name,context)

class AddListdoView(CreateView):
    template_name = 'Notes/listdo_create.html'
    form_class = ListDoForm

    def get_context_data(self, **kwargs):
        context = super(AddListdoView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ListContentFormSet(self.request.POST)
        else:
            context['formset'] = ListContentFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('Notes:index')  # assuming your model has ``get_absolute_url`` defined.
        else:
            #return self.render_to_response(self.get_context_data(form=form))
            return render(request,self.template_name,self.get_context_data(form=form))

def UpdateListdoView(request, listdo_id):
    listdo = ListDo.objects.get(pk=listdo_id)
    form = ListDoForm()
    if request.method == "POST":
    	form = ListDoForm(request.POST)
    	formset = ListContentFormSet(request.POST, request.FILES, instance=listdo)
    	if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return redirect('Notes:index')
    else:
        formset = ListContentFormSet(instance=listdo)
        form = ListDoForm(instance=listdo)
    return render(request, 'Notes/listdo_update.html', {'formset': formset,'form': form})

class ListDoDelete(DeleteView):
 	model = ListDo
 	success_url = reverse_lazy('Notes:index')

class TagView(ListView):
	template_name = 'Notes/tagview.html' 
	context_object_name = 'all_user_tags'
	def get_queryset(self):
		p_user=get_current_user()
		return Tag.objects.filter(users=p_user)

class TagUpdate(UpdateView):
	model = Tag
	fields = ['tag_title'] 

class TagDelete(DeleteView):
	model = Tag
	success_url = reverse_lazy('Notes:tag-view')			

class TagCreate(CreateView):
	form_class = TagForm
	template_name ='Notes/tag_form.html'		
	#display blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	#process form Data	
	def post (self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			#cleaned(Normalized) data
			title = form.cleaned_data['tag']
			#tag.save()
			#all_tag= Tag.objects.filter(tag_title=tag.tag_title)
			tag, dummy = Tag.objects.get_or_create(tag_title=title)
			user=get_current_user()
			#for tag in all_tag:
			#usertag, created = UserTag.objects.get_or_create(tag.tag_title=tag)
			user.tag_set.add(tag)
			user.save()
			#tag1.save()
			return redirect('Notes:tagview')

		return render(request,self.template_name,{'form':form})	

		





		


