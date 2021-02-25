from django.db.models.signals import pre_save

from django.dispatch import receiver

from apps.utils.helpers import unique_slug_generator

from .models import Post, Comment


@receiver(pre_save, sender=Post)
def pre_save_add_post_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Comment)
def pre_save_add_comment_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
