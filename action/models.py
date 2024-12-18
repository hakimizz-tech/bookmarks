from dataclasses import fields

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.


class Action(models.Model):
    user = models.ForeignKey(  #The user who performed the action
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='actions'
    )

    verb = models.CharField(max_length=250)          #The action that the user performed
    created = models.DateTimeField(auto_now_add=True) #The date and time the action was performed

    target_ct = models.ForeignKey(
        ContentType,
        blank = True,
        null = True,
        related_name='target_obj',
        on_delete=models.CASCADE,
    )

    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['target_ct', 'target_id'])
        ]

    def __str__(self):
        return f"{self.user} performed {self.verb} action"