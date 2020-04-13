from django import forms
from tasks.models import Tasks


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'overview', 'description')
