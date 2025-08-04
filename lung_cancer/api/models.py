from django.db import models

# Create your models here.
class UserHistory(models.Model):
    name = models.CharField(max_length=100)
    previous_mri_scan = models.ImageField(null=True, blank=True)
    previous_user_data = models.JSONField(null=True, blank=True)
    previous_ai_suggestions = models.TextField(null=True, blank=True)