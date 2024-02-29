from django import forms

from .models import Project, Tech

class ProjectForm(forms.ModelForm):
    tech = forms.ModelMultipleChoiceField(
        queryset=Tech.objects.all(),
        widget=forms.SelectMultiple
    )
    class Meta:
        model = Project
        fields = '__all__'