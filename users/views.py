from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm



# Create your views here.
def register(request):
    '''
    view function for registering 
    '''
    if request.method=='POST':
         form=UserRegistrationForm(request.POST)

         if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             messages.success(request,f'Account for {username} created!')
             return redirect('awards-home')

    else:
        form=UserRegistrationForm()
    
    return render(request,'users/registration.html',{'form':form})


