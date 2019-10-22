from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from projects.models import Projects
from django.contrib.auth.forms import UserCreationForm





class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProjectForm(forms.ModelForm):

    class Meta:
        model= Projects
        exclude= ['author', 'created_date', 'author_profile']

