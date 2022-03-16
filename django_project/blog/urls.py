from unicodedata import name
from django.urls import path
from .views import (
    CategorySadPostListView, 
    CategoryLovePostListView, 
    CategoryLifePostListView, 
    CategoryNaturePostListView, 
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
    UserCommentListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view() , name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name = 'post-detail'),
    path('post/<int:fav_id>/add-favorite', views.add_favorite , name = 'add-favorite'),
    path('post/<int:fav_id>/remove-favorite', views.remove_favorite , name = 'remove-favorite'),
    path('post/new/', PostCreateView.as_view() , name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name = 'post-delete'),
    path('user/<str:username>', UserPostListView.as_view() , name = 'user-posts'),
    path('category/Sad', CategorySadPostListView.as_view() , name = 'category-sad-posts'),
    path('category/Nature', CategoryNaturePostListView.as_view() , name = 'category-nature-posts'),
    path('category/Life', CategoryLifePostListView.as_view() , name = 'category-life-posts'),
    path('category/Love', CategoryLovePostListView.as_view() , name = 'category-love-posts'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view() , name = 'comment-create')
]
