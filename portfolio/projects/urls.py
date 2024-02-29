from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('projects/', projectsListView.as_view(), name='index')
]
