from django import forms
from django.forms import ModelForm
from .models import Posts

class PostForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = [
			'title',
			'content',
			'is_public']
