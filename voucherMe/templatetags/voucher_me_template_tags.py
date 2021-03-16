from django import template
from voucherMe.models import Post

register = template.Library()

@register.inclusion_tag('voucher/posts.html')
def get_posts_list(current_post=None):
    return {'posts': Post.objects.all(),
            'current_post': current_post}