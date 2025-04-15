from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.users.manager import UserManager

    
class User(AbstractUser):
    username = None
    last_login = None
    first_name = models.CharField("First Name", max_length=127, blank=True, null=True)
    last_name = models.CharField("First Name", max_length=127, blank=True, null=True)
    email = models.EmailField("email address", unique=True, db_index=True)
    is_employed = models.BooleanField(default=True)
    note = models.TextField(default="", blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='user_groups',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='user_permissions',
        blank=True
    )

    objects = UserManager() 
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.is_test}"