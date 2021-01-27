from django.urls import path
from .views import *

urlpatterns = [
    path('', edu_list, name='edu_list_url'),
    path(
        'undergraduate/<str:slug>/', program_detail,
        name='bachelor_program_detail_url'
    ),
    path(
        'master/<str:slug>/', program_detail,
        name='master_program_detail_url'
    ),
    path('phd/<str:slug>/', program_detail, name='phd_program_detail_url'),
]
