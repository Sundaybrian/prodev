from django.urls import path
from .views import (PostCreateView)
from . import views

urlpatterns=[
    path('',views.home,name='awards-home'),
    path('post/<int:pk>/',views.postDetail,name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-new')
]