from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username']
    widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2'}),
            'username': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded px-3 py-2'}),
        }

class ProfileImageForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image']