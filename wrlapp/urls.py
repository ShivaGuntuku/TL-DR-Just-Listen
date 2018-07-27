from django.urls import path

from . import views

app_name = 'wrlapp'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.show_all, name='show'),
    path('create', views.create_post, name='create'),
    path('view/<int:id>', views.retrive_post, name='retrive'),
    path('<int:id>/update', views.update_post, name='update'),
    path('<int:id>/delete', views.delete_post, name='delete'),
]