from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
