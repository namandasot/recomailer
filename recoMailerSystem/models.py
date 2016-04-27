from django.db import models
from email import email

# Create your models here.
class User(models.Model):
    unique_cookie_id = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, blank= True, null=True)
    modified = models.DateTimeField(auto_now=True, blank= True, null=True)

class Lead(models.Model):
    project_no = models.IntegerField()
    user = models.ForeignKey(User)
    lmsResponseNo = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank= True, null=True)
    
class FilledLeads(models.Model):
    project_no = models.IntegerField()
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, blank= True, null=True)
    