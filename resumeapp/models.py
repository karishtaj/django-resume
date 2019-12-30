from django.db import models

# Create your models here.
class resumedetails(models.Model):
    Career_Objective=models.CharField(max_length=200)
    Educational_Qualifications=models.CharField(max_length=200)
    Technical_Skills=models.CharField(max_length=200)
    Key_Strengths=models.CharField(max_length=200)
    Academic_Project=models.CharField(max_length=200)
    Personal_Details=models.CharField(max_length=200)
    Declaration=models.CharField(max_length=200)
    Signature=models.CharField(max_length=200)
    