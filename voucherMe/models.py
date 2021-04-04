# AARYAN

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

TAGS_CATEGORY = (
    ("1", "FOOD"),
    ("2", "TRAVEL"),
    ("3", "FASHION"),
    ("4", "TECHNOLOGY"),
    ("5", "BOOKS"),
    ("6", "MUSIC"),
    ("7", "FURNITURE"),
    ("8", "STATIONARY & ART"),
    ("9", "SKINCARE & BEAUTY"),
)
TAGS_TYPE = (
    ("1", "FLASH SALE/DISCOUNT"),
    ("2", "BUY MORE, SAVE MORE"),
    ("3", "LOTTERY/COMPETITION"),
    ("4", "GIFT BUNDLE/GIVEAWAY"),
    ("5", "BUY 1 GET 1 FREE"),
    ("6", "LOYALTY PROGRAM"),
    ("7", "VOUCHER/COUPON"),
    ("8", "FREE SHIPPING/RETURN"),
    ("9", "OTHER"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1024, unique=False)
    image = models.ImageField(upload_to='business_images', blank=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Businesses'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Business, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    promo = models.CharField(max_length=50, blank=True)
    tags_category = models.CharField(max_length=32, choices=TAGS_CATEGORY, default=1)
    tags_type = models.CharField(max_length=32, choices=TAGS_TYPE, default=1)
    visits = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        for field_name in ['promo']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Post, self).save(*args, **kwargs)