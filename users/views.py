from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    '''
    view function for registering 
    '''
    form=UserCreationForm()
    return render(request,'users/registration.html',{'form':form})
    

