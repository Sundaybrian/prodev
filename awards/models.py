from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your models here.

class Post(models.Model):
    '''
    
    '''
    title=models.CharField(max_length=30)
    description=models.TextField()
    link=models.CharField()
    image=models.ImageField(upload_to='poster/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Post{self.title}--{self.description}--{self.author.username}'
        
