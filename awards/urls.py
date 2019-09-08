from django.urls import path
from .views import (PostCreateView,PostUpdateView,PostDeleteView,HomeListView,UserPostListView)
from . import views

urlpatterns=[
    path('',HomeListView.as_view(),name='awards-home'),
    path('user/<str:username>/posts',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',views.postDetail,name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-new'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('search/',views.search_results,name='search-results'),
]