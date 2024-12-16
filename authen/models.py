from django.db import models
from django.contrib.auth.models import AbstractUser


class user_forms(AbstractUser):

    
    address=models.CharField( max_length=50)


