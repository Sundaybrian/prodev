from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from users.models import Profile


# 
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    '''
    
    '''
    title=models.CharField(max_length=30)
    description=models.TextField()
    link=models.CharField(max_length=100)
    image=models.ImageField(upload_to='poster/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    design=models.IntegerField(blank=True,default=0)
    usability=models.IntegerField(blank=True,default=0)
    creativity=models.IntegerField(blank=True,default=0)
    content=models.IntegerField(blank=True,default=0)
    mobile=mobile.IntegerField(blank=True,default=0)
    
    def __str__(self):
        return f'Post{self.title}--{self.description}--{self.author.username}'

    def get_absolute_url(self):
        '''
            return full path of a url
        '''    
        return reverse('post-detail',kwargs={'pk':self.pk}) 



    def save_post(self):
        '''
        method to save a post
        '''
        self.save()

    @classmethod
    def get_posts(cls):
        '''
            method to fetch all posts
        '''
        posts=cls.objects.order_by('date_posted')
        return posts   

    @classmethod
    def get_post_by_id(cls,id):
        try:

            post=cls.objects.get(id=id)
        except ObjectDoesNotExist:

            raise Http404()
            assert False

        return post  

    @classmethod
    def get_posts_by_username(cls,username):

        posts=cls.objects.filter(author=username).order_by('-date_posted')
        return posts
          

    @classmethod
    def delete_post(cls,post_id):
        '''
            method to delete a post
        '''
        img=cls.objects.get(id=post_id).delete()    

    @classmethod
    def search(cls,search_term):
        '''
            method that returns a post based on search query
        '''
        posts=cls.objects.filter(Q(title__icontains=search_term) |Q(author__username__icontains=search_term))   
        return posts


class Review(models.Model):
    '''
    '''
    design=models.IntegerField(blank=True,default=0)
    usability=models.IntegerField(blank=True,default=0)
    creativity=models.IntegerField(blank=True,default=0)
    content=models.IntegerField(blank=True,default=0)
    mobile=mobile.IntegerField(blank=True,default=0)
    post=models.ForeignKey(Project,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

            













