from django.urls import path
from django.conf.urls import url
from .views import (PostCreateView,PostUpdateView,PostDeleteView,UserPostListView)
from . import views

urlpatterns=[
    path('',views.home,name='awards-home'),
    path('user/<str:username>/posts',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',views.postDetail,name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-new'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('search/',views.search_results,name='search-results'),
    url(r'^api/posts/$', views.PostList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
]