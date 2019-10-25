from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from projects.models import Projects,Profile
from django.contrib.auth.forms import UserCreationForm





class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class ProjectForm(forms.ModelForm):

    class Meta:
        model= Projects
        exclude= ['author', 'created_date', 'author_profile']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

