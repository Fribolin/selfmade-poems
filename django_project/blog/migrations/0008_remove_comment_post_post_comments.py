# Generated by Django 4.0.3 on 2022-03-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_comments_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='blog.comment'),
        ),
    ]