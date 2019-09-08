from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Post,Review
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewReviewForm
from django.contrib import messages
from .models import Post,Review
from users.models import Profile


# using django generic views
from django.views.generic import (CreateView,DeleteView,UpdateView,ListView)

#login required mixins to add login required to the class based views
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# area api
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer
from .serializer import ProfileSerializer
from rest_framework import status

@login_required
def home(request):

    sites_list=Post.get_posts()
    paginator = Paginator(sites_list, 5)
    page = request.GET.get('page')
    sites = paginator.get_page(page)

    return render(request,'awards/home.html',{'sites':sites})

# class HomeListView(ListView):
#     '''
#         refactoring the home view function with a class based view
#     '''
#     model=Post
#     template_name='awards/home.html'
#     context_object_name='sites'
#     ordering=['-date_posted']
#     paginate_by=4



class UserPostListView(ListView):
    '''
        class view to render a single user posts
    '''
    model=Post
    template_name='awards/user-posts.html'
    context_object_name='sites'
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        '''

        '''
        user= get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.get_posts_by_username(user)



def postDetail(request,pk):
    '''
    view function that leads to a single post
    '''

    post=Post.get_post_by_id(pk)
    reviews=Review.get_all_reviews(pk)

    post.design=reviews['design']
    post.usability=reviews['usability']
    post.creativity=reviews['creativity']
    post.content=reviews['content']
    post.mobile=reviews['mobile']
    post.average_review=reviews['average_review']

    post.save()


    current_user=request.user
    if request.method=='POST':
        form=NewReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.judge=current_user
            review.post=post
            
            review.save()
            messages.success(request,f'Review Submitted')

            return redirect('post-detail',pk)

    else:
        form=NewReviewForm()  

    context={
        'site':post,
        'form':form
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


def search_results(request):
    '''
    view function that redirects to a search results page
    '''
    if 'site' in request.GET and request.GET['site']:
        search_term=request.GET.get('site')
        search_posts=Post.search(search_term)
        context={
            'message':f'{search_term}',
            'sites':search_posts
        }

        return render(request,'awards/search.html',context)
    else :
        return render(request,'awards/search.html')    


class PostList(APIView):
    def get(self,request,format=None):
        all_posts=Post.objects.all()
        serializers=PostSerializer(all_posts,many=True)
        return Response(serializers.data)

class PostDescription(APIView):
    '''
    Api view to fetch a single post
    '''        

    def get_post(self,pk):
        try:
            return Post.objects.get(pk=pk)

        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializers = PostSerializer(post)
        return Response(serializers.data)        
   


class ProfileList(APIView):

    def get(self,request,format=None):
        all_profiles=Profile.objects.all()
        serializers=ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)        




