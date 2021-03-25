from django import forms
from django.contrib.auth.models import User
from voucherMe.models import Business, Post, UserProfile


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

    class Meta:
        model = Business
        fields = ('name', 'description')
        exclude = ('user_id',)

class PostForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Your post's name goes here.")
    description = forms.CharField(widget=forms.Textarea, max_length=1024,
                                  help_text="What is this post about?")
    promo = forms.CharField(help_text="Add a promo code (if you want!)")
    tags_category = forms.CharField(widget=forms.CheckboxSelectMultiple)
    tags_type = forms.CharField(widget=forms.ChoiceField)
    visits = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Post
        fields = ('name', 'description', 'promo', 'tags_category', 'tags_type',)
        exclude = ('business_id',)