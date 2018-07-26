from django import forms
# from pagedown.widgets import PagedownWidget
from .models import Posts

class PostForm(forms.ModelForm):
	# content = forms.CharField(widget = PagedownWidget(show_preview = False))
	class Meta:
		models = Posts
		fields = [
			'title',
			'content']