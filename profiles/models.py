from django.contrib.auth.models import User
from django.db import models 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def created_user_profile(sender, created, instance, **kwargs):
        """Create a new Profile() object, when Django User is create."""
        if created:
            Profile.objects.create(user=instance)