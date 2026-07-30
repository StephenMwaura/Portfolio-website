from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    tech_stack = models.CharField(max_length= 150)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} < {self.email}>"
    

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    education = models.TextField()
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.name