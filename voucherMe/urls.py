#CHARLIE

from django.urls import path
from voucherMe import views

app_name = 'voucherMe'

urlpatterns = [
    path('', views.index, name='index'),
    path('business/<slug:business_name_slug>/', views.show_business, name='show_business'),
    path('business/<slug:business_name_slug>/<int:post_id>/', views.show_post, name='show_post')
]
