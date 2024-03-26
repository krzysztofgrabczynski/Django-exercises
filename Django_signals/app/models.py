from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models import signals
from django.forms.models import model_to_dict
from django.template.defaultfilters import slugify
import json
import os


User = get_user_model()


@receiver(signals.post_save, sender=User)
def user_model_post_save(sender, instance, created, **kwargs):
    if created:
        print("Send email to %s" % instance.username)
    else:
        print("%s just saved" % instance.username)


class Post(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    like = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return self.name


@receiver(signals.pre_save, sender=Post)
def post_model_pre_save(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(signals.pre_delete, sender=Post)
def post_modele_pre_delete(sender, instance, **kwargs):
    """
    Add deleted object to the `backup.json` file.
    """

    backup_path = "backup.json"
    fields = ["id", "name", "slug"]

    with open(backup_path, "r") as file:
        if os.path.getsize(backup_path) != 0:
            json_backup = json.load(file)
        else:
            json_backup = []

    with open(backup_path, "w") as file:
        json_backup.append(model_to_dict(instance, fields=fields))
        print(json_backup)
        file.write(json.dumps(json_backup, indent=4))


@receiver(signals.m2m_changed, sender=Post.like.through)
def post_model_like_changed(sender, instance, action, **kwargs):
    users = User.objects.filter(id__in=kwargs.get("pk_set"))

    if action == "post_remove":
        for user in users:
            print(f"{user} user removed like under {instance} post")
    elif action == "post_add":
        for user in users:
            print(f"{user} user add like under {instance} post")
