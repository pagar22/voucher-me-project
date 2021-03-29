from django import forms
from django.contrib.auth.models import User
from voucherMe.models import Business, Post, UserProfile

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

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    owner = forms.BooleanField(widget=forms.HiddenInput)
    class Meta:
        model = UserProfile
        fields = ('picture',)


class BusinessForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="What's your business called?")
    description = forms.CharField(widget=forms.Textarea, max_length=1024,
                                  help_text="Add a catchy description for your business!")
    slug = forms.CharField(widget=forms.HiddenInput, required=False)
    image = forms.ImageField(help_text="Attach a logo!", required=False)

    class Meta:
        model = Business
        fields = ('name', 'description')
        exclude = ('user',)

class PostForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Your post's name goes here.")
    description = forms.CharField(widget=forms.Textarea, max_length=1024,
                                  help_text="What is this post about?")
    promo = forms.CharField(max_length=50, help_text="Add a promo code (if you want!)", required=False)
    tags_category = forms.ChoiceField(help_text="Add a category tag", choices=TAGS_CATEGORY)
    tags_type = forms.ChoiceField(help_text="Add a type tag", choices=TAGS_TYPE)
    visits = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Post
        fields = ('name', 'description', 'promo', 'tags_category', 'tags_type',)
        exclude = ('business', 'visits',)