#AARYAN

from django.shortcuts import render
from datetime import datetime
from voucherMe.models import Post

def index(request):
    post_list = Post.objects.order_by('-votes')[:10]
    context_dict = {}
    context_dict['posts'] = post_list
    vistor_cookie_handler(request)
    return render(request, 'voucher/index.html', context=context_dict)

def about(request):
    vistor_cookie_handler(request)
    context_dict = {}
    context_dict['visits'] = request.session['visits']
    return render(request, 'voucher/about.html', context=context_dict)

#cookie handler
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
