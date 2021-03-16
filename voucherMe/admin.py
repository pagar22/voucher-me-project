# CHARLIE

from django.contrib import admin
from voucherMe.models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post, PostAdmin)
