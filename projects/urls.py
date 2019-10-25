from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url,include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,ReviewCreateView
from . import views
urlpatterns = [
    path('',  PostListView.as_view(), name='projects-index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('review/new/<int:pk>/', ReviewCreateView.as_view(), name='review-create'),


]
