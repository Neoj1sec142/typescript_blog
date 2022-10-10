from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(default="Not Entered Yet")
    user_type = models.CharField(max_length=50, default="Not Entered Yet")
    location = models.CharField(max_length=150, default="Not Entered Yet")
    ig = models.CharField(max_length=50, default="Not Entered Yet")
    mm = models.CharField(max_length=50, default="Not Entered Yet")
    def __str__(self):
        return self.user_type
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()