from django.shortcuts import render
from django.http import HttpResponse
from .email import send_welcome_email
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images":images})