# AARYAN

from django.shortcuts import render
from datetime import datetime
from voucherMe.models import UserProfile, Business, Post


# pageviews
def index(request):
    post_list = Post.objects.order_by('-votes')[:10]
    tags_category = Post.objects.get().tags_category
    tags_type = Post.objects.get().tags_type
    context_dict = {}
    context_dict['posts'] = post_list
    context_dict['tags_category'] = tags_category
    context_dict['tags_type'] = tags_type
    vistor_cookie_handler(request)
    return render(request, 'voucher/index.html', context=context_dict)


def about(request):
    vistor_cookie_handler(request)
    context_dict = {}
    context_dict['visits'] = request.session['visits']
    return render(request, 'voucher/about.html', context=context_dict)


def show_business(request, business_name_slug):
    context_dict = {}
    try:
        business = Business.objects.get(slug=business_name_slug)
        posts = Post.objects.filter(business_id=business)
        context_dict['business'] = business
        context_dict['posts'] = [posts]
    except Business.DoesNotExist:
        context_dict['business'] = None
        context_dict['posts'] = None
    return render(request, 'voucher/business.html', context=context_dict)


# how to uniquely identify post
def show_post(request, business_name_slug, post_id):
    context_dict = {}
    try:
        business = Business.objects.get(slug=business_name_slug)
        post = Post.objects.get(id=post_id)
        context_dict['business'] = business
        context_dict['post'] = post
    except Post.DoesNotExist:
        context_dict['business'] = None
        context_dict['post'] = None
    return render(request, 'voucher/post.html', context=context_dict)


# cookie handler
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def vistor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', 1))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits
