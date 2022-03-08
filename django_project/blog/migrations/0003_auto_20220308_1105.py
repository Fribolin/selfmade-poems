# Generated by Django 3.1.5 on 2022-03-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('SA', 'Sad'), ('LO', 'Love'), ('NA', 'Nature'), ('LI', 'Life')], default='', max_length=30),
        ),
    ]