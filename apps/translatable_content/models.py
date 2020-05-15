from django.db import models
from django.db.models.signals import pre_save
from tinymce.models import HTMLField

from .signals import slug_save_receiver
from .choices import LANGUAGE_CODES, MEDIA_TYPES

# Create your models here.

class Post(models.Model):
    title           = models.CharField(max_length=50)
    slug            = models.SlugField(unique=True, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + ' - ' + self.slug


class Media(models.Model):
    file_name        = models.CharField(max_length=100)
    url             = models.CharField(max_length=500)
    file_type        = models.CharField(
        max_length=15,
        choices=MEDIA_TYPES
    )

    def __str__(self):
        return self.file_name

class Tag(models.Model):
    name            = models.CharField(max_length=100)
    color_code      = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    post            = models.ForeignKey(Post, related_name='contents', on_delete=models.CASCADE)
    media           = models.ManyToManyField(Media, blank=True, null=True)
    tags            = models.ManyToManyField(Tag, blank=True, null=True)
    key             = models.CharField(max_length=70)
    value           = HTMLField()
    title           = models.CharField(max_length=120, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    order           = models.PositiveIntegerField(blank=True, null=True)
    language_code   = models.CharField(
        max_length=2,
        choices=LANGUAGE_CODES,
        default='en'
    )

    def __str__(self):
        return self.key + ' - ' + str(self.post.title)
       

# Signals
pre_save.connect(slug_save_receiver, sender=Post)