from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def favorite_post(request, fav_id):
    post = get_object_or_404(Post, id=fav_id)

    context = {
        'posts': Post.objects.all()
    }
    
    if request.method == 'POST': #Then add this video to users' favourite
        post.favorite.add(request.user)

    return redirect(request.META['HTTP_REFERER'])

def not_favorite_post(request, fav_id):
    post = get_object_or_404(Post, id=fav_id)

    context = {
        'posts': Post.objects.all()
    }
    
    if request.method == 'POST': #Then add this video to users' favourite
        post.favorite.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        return Post.objects.filter(author = user).order_by('-date_posted')
        
class CategorySadPostListView(ListView):
    model = Post
    template_name = "blog/sad.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class CategoryLifePostListView(ListView):
    model = Post
    template_name = "blog/life.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class CategoryLovePostListView(ListView):
    model = Post
    template_name = "blog/love.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class CategoryNaturePostListView(ListView):
    model = Post
    template_name = "blog/nature.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False

class CommentDetailView(DetailView):
    model = Comment

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    #fields = '__all__'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk = self.kwargs['pk'])
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False

class UserCommentListView(ListView):
    model = Comment
    template_name = "blog/user_comments.html"
    context_object_name = 'comments'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        return Comment.objects.filter(author = user).order_by('-date_posted')