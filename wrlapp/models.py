from django.conf import settings
from django.db import models

# Create your models here.
class Posts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 default = 1,
							 on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)
	content = models.TextField()
	read_time = models.TimeField(null = True, blank = True)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	create_date = models.DateTimeField(auto_now = False, auto_now_add = True)


# class Users(models.Model):
    