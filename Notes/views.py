from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
# Create your views here.
@login_required(login_url='/notes/login/')
def index(request):
	#current_user=request.user
	all_notes = Note.objects.filter(user=request.user)
	#template = loader.get_template('Notes/index.html')
	context = {'all_notes':all_notes,'user':request.user}
	return render (request,'Notes/index.html',context)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/notes/main_page')

def main_page(request):
	return render(request,'Notes/main_page.html')	