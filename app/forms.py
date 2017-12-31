from django import forms
from app.models import Profile

class ProfileForm(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=30)
    email = forms.EmailField(label='Your email')

    class Meta:
        model=Profile
        fields=['name','email']