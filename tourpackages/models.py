# models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100) 

    def str(self):
        return self.username  # To display the username in the admin panel