# forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    status = forms.ChoiceField(choices=Task.STATUS_CHOICES)  # Assuming STATUS_CHOICES is defined in your Task model

    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'status']
