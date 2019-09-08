from django import forms
from .models import Review

class NewReviewForm(forms.ModelForm):
    '''
    form to create a rating
    '''
    class Meta:
        model=Review
        exclude=['post','judge']
