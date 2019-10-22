from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    path('',  views.index, name='projects-index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
