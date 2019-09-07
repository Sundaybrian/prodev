from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# dummy data

sites=[
    {
       'dev':'Sunday Brian',
       'title':'Anitas Kitchen',
       'date_posted':'September 07,2019',
       'description':'lorem ipsum lorem ipsum',
       'link':'https://sundaybrian.github.io/anitas-kitchen-v2/' 
    },
        {
       'dev':'Sunday Priest',
       'title':'Birthday Version Lady',
       'date_posted':'September 07,2019',
       'description':'lorem ipsum lorem ipsum',
       'link':'https://sundaybrian.github.io/anitas-kitchen-v2/' 
    },
        {
       'dev':'Sunday Omwami',
       'title':'Anthem',
       'date_posted':'September 11,2019',
       'description':'lorem ipsum lorem ipsum',
       'link':'https://sundaybrian.github.io/anitas-kitchen-v2/' 
    },

]
def home(request):
    context={
        'sites':sites
    }
    return render(request,'awards/home.html',context)
