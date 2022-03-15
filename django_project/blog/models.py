from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.TextChoices):
    SAD = 'SA', ('Sad')
    LOVE = 'LO', ('Love')
    NATURE = 'NA', ('Nature')
    LIFE = 'LI', ('Life')

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    category = models.CharField(max_length = 30, choices=Category.choices, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name="fav_posts", blank=True)
    #comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    name = models.CharField(max_length=80, default="")
    body = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", default="")
    


