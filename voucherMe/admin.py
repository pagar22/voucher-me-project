
from django.contrib import admin
from voucherMe.models import UserProfile, Business, Post


class BusinessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_id')

admin.site.register(Business, BusinessAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)

