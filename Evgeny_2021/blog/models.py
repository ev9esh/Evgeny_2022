from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.Model()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
    author = models.CharField(max_length=30)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


