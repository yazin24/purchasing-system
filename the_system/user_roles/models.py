from django.db import models
from django.contrib.auth.models import User

class UserRoles(models.Model):
    USER_ROLES_CHOICES = (
        ('purchasing', 'Purchasing'),
        ('inventory', 'Inventory'),
        ('receiving', 'Receiving'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=20, choices=USER_ROLES_CHOICES)
