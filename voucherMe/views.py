# AARYAN
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import logout
from voucherMe.forms import BusinessForm, PostForm
from voucherMe.models import UserProfile, Business, Post


# pageviews
def index(request):
    post_list = Post.objects.order_by('-visits')[:10]
    business_list = Business.objects.order_by('-likes')[:10]
    context_dict = {}
    context_dict['posts'] = post_list
    context_dict['businesses'] = business_list
    return render(request, 'voucher/index.html', context=context_dict)


def about(request):
    context_dict = {}
    return render(request, 'voucher/about.html', context=context_dict)


# Add
def add_business(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    if user is None:
        return redirect('voucherMe:index')

    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user_id = user
            if 'image' in request.FILES:
                business.image = request.FILES['image']
            business.save()
            return redirect('voucherMe:index')
        else:
            print(form.errors)
    context_dict = {'form': form, 'user': user}
    return render(request, 'voucher/add_business.html', context_dict)

#how to get user object and assign value (not null), don't want to reassign new
def add_post(request, username, business_name_slug):
    try:
        business = Business.objects.get(slug=business_name_slug)
    except Business.DoesNotExist:
        business = None
    if business is None:
        return redirect('voucherMe:index')
    user = business.user_id
    form = PostForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.business_id = business
            post.save()
            return redirect('voucherMe:index')
        else:
            print(form.errors)
    context_dict = {'form': form, 'business': business}
    return render(request, 'voucher/add_post.html', context_dict)


# show
def show_business(request, business_name_slug):
    context_dict = {}
    try:
        business = Business.objects.get(slug=business_name_slug)
        posts = Post.objects.filter(business_id=business)
        context_dict['business'] = business
        context_dict['posts'] = posts
    except Business.DoesNotExist:
        context_dict['business'] = None
        context_dict['posts'] = None
    return render(request, 'voucher/business.html', context=context_dict)


def show_post(request, business_name_slug, post_id):
    context_dict = {}
    try:
        business = Business.objects.get(slug=business_name_slug)
        post = Post.objects.get(id=post_id)
        vistor_cookie_handler(request)
        post.visits = request.session['visits']
        context_dict['business'] = business
        context_dict['post'] = post
        context_dict['visits'] = post.visits
        context_dict['promo'] = post.promo
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


@login_required
    def user_logout(request):

    logout(request)

    return redirect(reverse('voucherMe:index'))
