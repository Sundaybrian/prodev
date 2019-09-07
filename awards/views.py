from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# dummy data

def home(request):
    context={
        'sites':Post.objects.all()
    }
    return render(request,'awards/home.html',context)
