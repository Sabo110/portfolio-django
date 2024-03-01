from django.db import models

# Create your models here.

class Tech(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="thumbnail")
    description = models.TextField(blank=False, null=False)
    demo_link = models.CharField(max_length=500, null=False, blank=False)
    github_link = models.CharField(max_length=500, null=True, blank=True)
    techs = models.ManyToManyField(Tech)

    



