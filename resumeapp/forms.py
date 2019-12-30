from django import forms
from resumeapp.models import resumedetails
class resumeform(forms.ModelForm):
    class Meta:
        model=resumedetails
        fields=['Career_Objective','Educational_Qualifications','Technical_Skills','Key_Strengths','Academic_Project','Personal_Details','Declaration','Signature']