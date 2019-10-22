from rest_framework import serializers
from .models import Projects,Profile

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('author','image','description','created_date','link','title','author_profile')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_picture','bio')