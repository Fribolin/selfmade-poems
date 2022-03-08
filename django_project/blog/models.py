from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.TextChoices):
    SAD = 'SA', ('Sad')
    LOVE = 'LO', ('Love')
    NATURE = 'NA', ('Nature')
    LIFE = 'LI', ('Life')

class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    category = models.CharField(max_length = 30, choices=Category.choices, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


