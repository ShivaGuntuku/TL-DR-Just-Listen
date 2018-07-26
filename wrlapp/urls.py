from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.show_all, name='Show Posts'),
    path('create', views.create_post, name='Create Post'),
    path('retrive', views.retrive_post, name='Retrive Post'),
    path('update', views.update_post, name='Update Post'),
    path('delete', views.delete_post, name='Delete Post'),
]