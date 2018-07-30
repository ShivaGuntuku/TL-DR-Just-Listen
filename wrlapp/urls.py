from django.urls import include, path

from . import views

app_name = 'wrlapp'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.show_all, name='show'),
    path('create', views.create_post, name='create'),
    path('view/<int:id>', views.retrive_post, name='retrive'),
    path('<int:id>/update', views.update_post, name='update'),
    path('<int:id>/delete', views.delete_post, name='delete'),
    path('how_it_work', views.how_it_work, name="work")
    # path(r'^accounts/', include('allauth.urls')),
]