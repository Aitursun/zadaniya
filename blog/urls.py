from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name = 'hello'),
    path('posts/', views.blog_all, name = 'posts'),
    path('postview/', views.PostView.as_view(), name='posts'),
    path('postview_detail/<int:id>/', views.blog_detail, name='show_detail'),

    path('postview/<int:id>/update/', views.PostUpdateView.as_view(), name='show_detail'),
    path('postview/<int:id>/delete/', views.PostDeleteView.as_view(), name='show_detail'),

    path('add-posts/', views.PostCreateView.as_view(), name='add postview'),
]