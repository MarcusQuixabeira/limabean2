from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
    path('', views.home, name='home'),
    path('researchers/', views.researchers, name='researchers'),
    path('researcher/<int:researcher_id>/', views.researcher_detail, name='researcher_detail'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]