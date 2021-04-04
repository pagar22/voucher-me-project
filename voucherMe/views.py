# AARYAN
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.urls import reverse
from django.contrib.auth import login
from voucherMe.forms import BusinessForm, PostForm
from voucherMe.models import UserProfile, Business, Post


# pageviews
def index(request):
    post_list = Post.objects.order_by('-visits')[:5]
    business_list = Business.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['posts'] = post_list
    context_dict['businesses'] = business_list

    return render(request, 'voucher/index.html', context=context_dict)


def about(request):
    context_dict = {}
    return render(request, 'voucher/about.html', context=context_dict)


@login_required
def profile(request, username):
    user = request.user
    userprofile, created = UserProfile.objects.get_or_create(user=user)
    businesses = Business.objects.filter(user_id=user).order_by('-likes')
    context_dict = {'user': user, 'userprofile': userprofile, 'businesses': businesses}
    return render(request, 'voucher/account.html', context=context_dict)


def search(request, type):
    context_dict = {}
    if request.method == 'GET':
        query = request.GET.get('search')
        query.strip()  # attempt to remove whitespaces
        try:
            if type == "business":
                result = Business.objects.filter(name__icontains=query).order_by('-likes')
            else:
                result = Post.objects.filter(name__icontains=query).order_by('-visits')
        except Business.DoesNotExist or Post.DoesNotExist:
            result = None
        context_dict['type'] = type
        context_dict['results'] = result
        return render(request, 'voucher/search.html', context=context_dict)
    return render(request, 'voucher/search.html', context=context_dict)


# Add
@login_required
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
            business.user = user
            if 'image' in request.FILES:
                business.image = request.FILES['image']
            business.save()
            return redirect('voucherMe:index')
        else:
            print(form.errors)
    context_dict = {'form': form, 'user': user}
    return render(request, 'voucher/add_business.html', context_dict)


@login_required
def add_post(request, business_name_slug):
    try:
        business = Business.objects.get(slug=business_name_slug)
    except Business.DoesNotExist:
        business = None
    if business is None:
        return redirect('voucherMe:index')
    user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if business:
                post = form.save(commit=False)
                post.business = business
                post.visits = 0
                post.save()
                return redirect(reverse('voucherMe:show_business',
                                        kwargs={'business_name_slug': business_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'business': business, 'user': user, }
    return render(request, 'voucher/add_post.html', context_dict)


# show
def all_businesses(request):
    business_list = Business.objects.order_by('-likes')
    context_dict = {'businesses': business_list}
    return render(request, 'voucher/all_businesses.html', context=context_dict)


def all_posts(request):
    posts_list = Post.objects.order_by('-visits')
    context_dict = {'posts': posts_list}
    return render(request, 'voucher/all_posts.html', context=context_dict)


def show_business(request, business_name_slug):
    context_dict = {}
    try:
        business = Business.objects.get(slug=business_name_slug)
        posts = Post.objects.filter(business_id=business).order_by('-visits')
        user = request.user
        context_dict['business'] = business
        context_dict['posts'] = posts
        context_dict['user'] = user
    except Business.DoesNotExist:
        context_dict['business'] = None
        context_dict['posts'] = None
        context_dict['user'] = None
    return render(request, 'voucher/business.html', context=context_dict)


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

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'voucher/post.html', context=context_dict)

def BusinessLike(request, pk):
    post = get_object_or_404(Business, id=request.POST.get('add_like'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

@login_required
def like_business(request):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['business']

    likes = 0
    if cat_id:
        business = business.objects.get(id=int(cat_id))
        if business:
            likes = business.likes + 1
            business.likes =  likes
            cat.save()
    return HttpResponse(likes)


# cookie handler
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits