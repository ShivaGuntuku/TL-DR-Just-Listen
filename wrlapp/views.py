from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions

from allauth.account.views import SignupView, LoginView
from rest_framework import generics
from .forms import PostForm
from .models import Posts
from .serializers import PostsSerializer

# JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class LoginView(generics.CreateAPIView):
	"""POST AUTH/login"""
	permission_classes = (permissions.AllowAny,)

	queryset = User.objects.all()

	def post(self, request, *args, **kwargs):
		username = request.data.get("username", "")
		password = request.data.get("password", "")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			# login saves the user’s ID in the session,
			# using Django’s session framework.
			login(request, user)
			serializer = TokenSerializer(data={
				# using drf jwt utility functions to generate a token
				"token": jwt_encode_handler(
					jwt_payload_handler(user)
				)})
			serializer.is_valid()
			return Response(serializer.data)
		return Response(status=status.HTTP_401_UNAUTHORIZED)

class ListPostsView(generics.ListAPIView):
	"""
	Provides a get method handler.
	"""
	queryset = Posts.objects.all()
	serializer_class = PostsSerializer
	permission_classes = (permissions.IsAuthenticated,)


def show_all(request):
	queryset_list = Posts.objects.all()
	if not request.user.is_authenticated:
		queryset_list = queryset_list.filter(
			   Q(is_public = True))
		context = {
			'queryset_list':queryset_list,
		}
	else:
		queryset_list = queryset_list.filter(
			   Q(user_id = request.user.id))
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