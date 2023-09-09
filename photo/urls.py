# urls.py는 photo가 아닌 myweb안에 있다 
# 프로젝트 전체의 url은 myweb/urls.py에서 photo안에 url은 photo/urls.py에서

from django.urls import path
from . import views

urlpatterns = [
    path("", views.photo_list, name='photo_list'),
    path('photo/<int:pk>/' , views.photo_detail, name = 'photo_detail'),
    path('photo/new/', views.photo_post, name = 'photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name = 'photo_edit'),
]
