from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# dummy data

def home(request):
    context={
        'sites':Post.get_posts()
    }
    return render(request,'awards/home.html',context)


def postDetail(request,pk):
    '''
    view function that leads to a single post
    '''

    post=Post.get_post_by_id(pk)
    context={
        'post':post,
    }

    return render(request,'awards/post-detail.html',context)