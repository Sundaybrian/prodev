from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='awards-home'),
    path('post/<int:pk>/',views.postDetail,name='post-detail'),
    path('post/new/',views.PostCreateView,name='post-new')
]