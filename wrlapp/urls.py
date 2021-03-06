from django.urls import include, path, re_path

from . import views
from .views import ListPostsView,LoginView

app_name = 'wrlapp'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.show_all, name='show'),
    path('create', views.create_post, name='create'),
    path('view/<int:id>', views.retrive_post, name='retrive'),
    path('<int:id>/update', views.update_post, name='update'),
    path('<int:id>/delete', views.delete_post, name='delete'),
    path('how_it_work', views.how_it_work, name="work"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('medium/view/<int:id>', views.retriveMediumContent, name='mediumViewOneContent'),
    re_path('^medium/view',  views.showMediumContent, name="mediumViewContent"),
    re_path('^medium/', views.getMediumContent, name="mediumCreateContent"),
    # path('posts/', ListPostsView.as_view(), name="posts-all")
    # path(r'^accounts/', include('allauth.urls')),
]