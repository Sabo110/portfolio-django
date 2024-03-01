from django.shortcuts import render
from django.views.generic import ListView

from .models import Project
# Create your views here.

def index(request):
    return render(request, 'index.html')

class projectsListView(ListView):
    model = Project
    template_name = 'projects.html'
    paginate_by = 6

def about(request):
    return render(request, 'about.html')
