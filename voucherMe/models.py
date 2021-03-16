# AARYAN

from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=1024, unique=False)
    votes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name
