from unicodedata import name
from django.urls import path
from .views import (
    CategoryPostListView, 
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView, 
    CommentDetailView, 
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView, 
    UserCommentListView,)
from . import views

urlpatterns = [
    path('', PostListView.as_view() , name = 'blog-home'),
    path('about/', views.about , name = 'blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view() , name = 'post-detail'),
    path('post/new/', PostCreateView.as_view() , name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name = 'post-delete'),
    path('user/<str:username>', UserPostListView.as_view() , name = 'user-posts'),
    path('category/<str:category>', CategoryPostListView.as_view() , name = 'category-posts'),

    path('post/<int:pk>/comment/new/', CommentCreateView.as_view() , name = 'comment-create')
]
