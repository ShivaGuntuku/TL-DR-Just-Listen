from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from allauth.account.views import SignupView, LoginView
from .forms import PostForm
from .models import Posts


def show_all(request):
	queryset_list = Posts.objects.all()
	context = {
		'queryset_list':queryset_list,
	}
	return render(request, 'index.html', context)


@login_required(login_url='/accounts/login/')
def create_post(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Post Successfully Created")
		return redirect("wrlapp:show")
	context = {
		'form' : form
	}
	return render(request,'create_post.html', context)


def retrive_post(request,id):
	queryset_list = Posts.objects.filter(id = id)
	context = {
		'queryset_list': queryset_list
	}
	return render(request,'retrive_post.html', context)


@login_required(login_url='/accounts/login/')
def update_post(request,id):
	instance = Posts.objects.filter(id = id).first()
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "Post is Updated.")
		return HttpResponseRedirect('/view/%d'%id)
	context = {
		'title' : instance.title,
		'instance' : instance,
		'form' : form
	}
	return render(request,'update_post.html', context)

@login_required(login_url='/accounts/login/')
def delete_post(request, id):
	instance = Posts.objects.get(id=id)
	instance.delete()
	messages.success(request, "Post is Deleted.")
	return redirect("wrlapp:show")


def how_it_work(request):
	context = {}
	return render(request, 'how_it_works.html', context)





class MySignupView(SignupView):
    template_name = 'my_signup.html'


class MyLoginView(LoginView):
    template_name = 'my_login.html'