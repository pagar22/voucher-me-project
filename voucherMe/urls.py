#CHARLIE

from django.urls import path
from voucherMe import views

app_name = 'voucherMe'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('account/<str:username>', views.account, name='account'),
    path('<str:username>/business/add_business/', views.add_business, name='add_business'),
    path('business/<slug:business_name_slug>/', views.show_business, name='show_business'),
    path('<str:username>/business/<slug:business_name_slug>/add_post/', views.add_post, name='add_post'),
    path('business/<slug:business_name_slug>/<int:post_id>/', views.show_post, name='show_post'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    #path('logout/', views.user_logout, name='logout'),

]
