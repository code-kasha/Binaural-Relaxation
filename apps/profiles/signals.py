from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth import get_user_model
from apps.profiles.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def post_save_create_profile(sender, created, instance, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    try:
        if not instance.profile:
            pass
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
