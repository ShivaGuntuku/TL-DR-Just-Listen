from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm
from .models import Posts

# ops: CRUDL
# create_post.html
# update_post.html
# retrive_post.html


def show_all(request):
	queryset_list = Posts.objects.all()
	context = {
		'queryset_list':queryset_list,
	}
	return render(request, 'index.html', context)

def create_post(request):
	context = {}
	return render(request,'create_post.html', context)

def retrive_post(request):
	context = {}
	return render(request,'retrive_post.html', context)

def update_post(request):
	context = {}
	return render(request,'update_post.html', context)

def delete_post(request):
	return HttpResponse('You can Delete post here.')
