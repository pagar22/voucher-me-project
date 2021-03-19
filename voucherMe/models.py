# AARYAN

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Business(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1024, unique=False)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Businesses'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Business, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=1024, unique=False)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name