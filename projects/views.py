from django.shortcuts import render,redirect
from django.http import HttpResponse

from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from users.forms import ProjectForm
from .models import *
# Create your views here.
def index(request):
  
    return render(request,'index.html')



@login_required
def postproject(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('/')
    else:
        form = ProjectForm()
    context = {
        'form':form,
    }
    return render(request, 'create-project.html', context)

def get_project(request, id):
    project = Projects.objects.get(pk=id)

    return render(request, 'project.html', {'project':project})
