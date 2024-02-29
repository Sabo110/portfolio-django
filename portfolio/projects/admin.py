from django.contrib import admin
from django.utils.html import format_html

from .models import *
from .forms import ProjectForm
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_techs','lien_github', 'demo')  

    def get_techs(self, obj):
        return " - ".join([str(p) for p in obj.techs.all()])
    get_techs.short_description = 'technologies'
    
    def lien_github(self, obj):
       return format_html('<a href="{}" target="_blank">{}</a>', obj.github_link, obj.github_link)
    
    def demo(self, obj):
       return format_html('<a href="{}" target="_blank">{}</a>', obj.demo_link, obj.demo_link)

@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    list_display = ('name',)  
