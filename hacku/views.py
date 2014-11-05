from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from forms import UserForm
from django.contrib.auth.models import User

def index(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid() :
			new_user = User.objects.create_user(**form.cleaned_data)
			return HttpResponseRedirect('/')
		else :
			print "Badluck"
	else:
		form = UserForm() 
	
	return render(request, 'index.html', {'form': form})