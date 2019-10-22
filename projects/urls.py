from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    path('',  views.index, name='projects-index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),

]
