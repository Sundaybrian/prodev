from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# using django generic views
from django.views.generic import (CreateView,DeleteView,UpdateView)

#login required mixins to add login required to the class based views
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
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
        'site':post,
    }

    return render(request,'awards/post-detail.html',context)


class PostCreateView(LoginRequiredMixin,CreateView):
    '''
        using class based view to create a post
        args:CreateView from django.views.generic

        success_url returns you to the homepage after succes creation of a post

    ''' 
    model=Post
    fields=['title','description','link','image'] 
    template_name='awards/post-new.html'  
    success_url='/'

    def form_valid(self,form):
        '''
            setting up the user instance to the form being submitted so it doesnt raise the intergrity error
        '''
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):  
    '''
        using class based view to create a post
        args:CreateView from django.views.generic

    ''' 
    model=Post
    fields=['title','description','link','image'] 
    template_name='awards/post-new.html'  
    

    def form_valid(self,form):
        '''
            setting up the user instance to the form being submitted so it doesnt raise the intergrity error
        '''
        form.instance.author=self.request.user
        return super().form_valid(form)   

    def test_func(self):
        '''
            grab the current post obj and check if current user is the author of the post
        '''
        post=self.get_object()

        if self.request.user==post.author:
            return True
        return False    


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    context_object_name='site'
    template_name='awards/post-confirm-delete.html'

    def test_func(self):
        '''
            grab the current post obj and check if current user is the author of the post
        '''
        post=self.get_object()

        if self.request.user==post.author:
            return True
        return False 


    