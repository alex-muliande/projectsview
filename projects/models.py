from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='users/', default='user.png')
    bio = models.TextField(default="Welcome!")

    def __str__(self):
        return f'{self.user.username} Profile' 
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)




class Projects(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='profile_pics/')
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    link = models.URLField()
    author_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='1', blank = True)

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.author} Post'

    class Meta:
        db_table = 'project'
        ordering = ['-created_date']

    def delete_project(self):
        self.delete()

    @classmethod
    def search_projects(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    @classmethod
    def get_project(cls,id):
        try:
            project = Projects.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return Project

    @property
    def design(self):
        if self.reviews.count() == 0:
            return 5
        return sum([r.design for r in self.reviews.all()]) / self.reviews.count()


    @property
    def usability(self):
        if self.reviews.count() == 0:
            return 5
        return sum([r.usability for r in self.reviews.all()]) / self.reviews.count()
    
    @property
    def creativity(self):
        if self.reviews.count() == 0:
            return 5
        return sum([r.creativity for r in self.reviews.all()]) / self.reviews.count()

    @property
    def content(self):
        if self.reviews.count() == 0:
            return 5
        return sum([r.content for r in self.reviews.all()]) / self.reviews.count()



    # @property 
    # def usability(self):
    #     user = Review.objects.all().aggregate(models.Avg('usability'))['usability__avg']
    #     return user
    



class Review(models.Model):
    ratings = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='reviews')
    design = models.IntegerField(choices=ratings, default=0)
    usability = models.IntegerField(choices=ratings, default=0)
    creativity = models.IntegerField(choices=ratings, default=0)
    content =  models.IntegerField(choices=ratings, default=0)
    overall_score = models.IntegerField(blank=True, default=0)

    def save_rate(self):
            self.save()

    def delete_rate(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('projects-index')

  


