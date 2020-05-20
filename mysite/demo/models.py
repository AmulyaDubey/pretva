from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from datetime import datetime

class Profile(models.Model):
    
    username=models.CharField(max_length=100, db_column='username', null=True)
    email = models.EmailField(max_length=150, db_column='email', null=True, unique=True)
    city=models.CharField(max_length=100, db_column='city', null=True)
    company=models.CharField(max_length=100, db_column='company', null=True)
    category=models.CharField(max_length=100, db_column='category', null=True)
    user_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, db_column='user_id')

    def __str__(self):
        return self.username