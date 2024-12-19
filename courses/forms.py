from django import forms
from .models import Course

class courseEntryForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor','image']

