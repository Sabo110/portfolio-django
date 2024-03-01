from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.
import os

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

@receiver(post_delete, sender=Project)
def delete_thumbnail(sender, instance, **kwargs):
    """
    Supprime le fichier thumbnail du système de fichiers
    quand l'instance de Project correspondante est supprimée.
    """
    # Vérifiez si un thumbnail existe
    if instance.thumbnail:
        # Construisez le chemin complet du fichier
        file_path = instance.thumbnail.path
        # Supprimez le fichier
        if os.path.isfile(file_path):
            os.remove(file_path)

    



