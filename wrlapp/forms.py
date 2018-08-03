from django import forms
from django.forms import ModelForm
from .models import Posts, FetchUrlContent

class PostForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = [
			'title',
			'content',
			'is_public']

class FetchUrlContentForm(forms.ModelForm):
	class Meta:
		model = FetchUrlContent
		fields = [
		'url']
		# 'getUrlContent']