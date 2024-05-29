from django import forms
from .models import Job
from .models import JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter', 'cv']        