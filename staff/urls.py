from django.urls import path
from .views import *

urlpatterns = [
    path('', members_list, name='members_list_url'),
    path('member/<str:slug>/', member_detail, name='member_detail_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_staff_detail_url'),
]
