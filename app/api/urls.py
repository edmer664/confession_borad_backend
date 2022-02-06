from django.urls import path
from . import views


urlpatterns = [
    path('get-posts/', views.get_posts, name='get_posts'),
    path('make-post/', views.make_post, name='make_post'),
    path('get-post/<int:post_id>/', views.get_post, name='get_post'),
]
