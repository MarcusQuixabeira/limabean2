from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Institution(models.Model):
  name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=20)

  def __str__(self):
    return self.short_name

class Researcher(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  bio = models.TextField(max_length=500)
  lattes_link = models.CharField(max_length=500)
  facebook_link = models.CharField(max_length=500, blank=True, null=True)
  instagram_link = models.CharField(max_length=500, blank=True, null=True)
  twitter_link = models.CharField(max_length=500, blank=True, null=True)
  institution = models.ForeignKey(Institution, models.SET_NULL, blank=True, null=True)
  photo = models.ImageField(upload_to='photos/researchers/')
  is_cover = models.BooleanField()

  def __str__(self):
    return self.first_name

class Article(models.Model):
  title = models.CharField(max_length=100)
  abstract = models.TextField(max_length=600)
  published_at = models.DateField()
  web_link = models.CharField(max_length=500)
  researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE)
  first_author = models.BooleanField()

  def __str__(self):
    return self.title

class Post(models.Model):
  title = models.CharField(max_length=100)
  subtitle = models.CharField(max_length=100)
  abstract = models.TextField(max_length=600)
  content = RichTextUploadingField()
  cover = models.ImageField(upload_to='photos/posts')
  published_at = models.DateField()
  is_cover = models.BooleanField()

  def __str__(self):
    return self.title

class ShortPost(models.Model):
  title = models.CharField(max_length=100)
  abstract = models.TextField(max_length=600)
  photo = models.ImageField(upload_to='photos/short_posts/')
  web_link = models.CharField(max_length=500)
  is_cover = models.BooleanField()

  def __str__(self):
    return self.title