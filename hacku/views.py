from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from forms import UserForm
from django.contrib.auth.models import User
from datetime import datetime
from hacku.models import *
from django.shortcuts import redirect
from datetime import datetime
from django.contrib.auth import login,logout,authenticate

def index(request):
	#logout(request)
	if request.method == "POST":
		username = request.POST['user1']
		password = request.POST['pass1']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
				# Redirect to a success page.
			else:
				print "Bie"
		else:
			print "Bie"
	ques_list=Question.objects.all()
	context = { 'ques_list':ques_list}
	return render(request, 'index.html', context)

def signup(request) :
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid() :
			new_user = User.objects.create_user(**form.cleaned_data)
			return HttpResponseRedirect('/')
		else :
			print "Badluck"
	else:
		form = UserForm() 
	context={'form': form}
	return render(request, 'signup.html', context)
def addQues(request):      #add Question
	print request.user.is_authenticated()
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == 'POST' :
		new_ques=Question(name=request.user.username,heading=request.POST.get('heading'),qText= request.POST.get('texting'),extra= request.POST.get('cate'))
		new_ques.save()
	context = {'name':request.user.username}
	return render(request, 'Comment.html',context)

def qdisplay(request, qComment_id):
	print request.user.is_authenticated()
	ques = get_object_or_404(Question, pk=qComment_id)
	if request.method == "POST":
		que=Question.objects.get(pk=qComment_id)
		que.votes+=1;
		que.save()
		new_ques=ques.comments_set.create(cName=request.user.username,cText=request.POST.get('cText'))
		new_ques.save()
		return HttpResponseRedirect('/'+qComment_id)
	context ={'ques' : ques, 'name':request.user.username}
	return render(request, 'Qdisplay.html',context)

def cat1(request) :
	cat1_list=Question.objects.filter(extra="Places")
	context = { 'cat1_list':cat1_list}
	return render(request, 'places.html', context)

def cat2(request) :
	cat2_list=Question.objects.filter(extra="Handsets")
	context = { 'cat2_list':cat2_list}
	return render(request, 'handsets.html', context)

def cat3(request) :
	cat3_list=Question.objects.filter(extra="Coding")
	context = { 'cat3_list':cat3_list}
	return render(request, 'coding.html', context)

def logout_v(request) :
	logout(request)
	context=""
	return HttpResponseRedirect('/')
	#if request.user is not None:
	#return HttpResponse("hhh")
	#else :
	#	return render(request, 'index.html', context)
