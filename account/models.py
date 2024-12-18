from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, default='users/default_profile/avatar-profile.jpg')

    def __str__(self):
        return f'Profile of {self.user.username}'

# This is an Intermediary model
class Contact(models.Model):
    # The user that creates the relationship
    user_from = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rel_from_set'
    )

    # The user that is being followed
    user_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rel_to_set'
    )

    # when the relationship was created
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort the results by the ordering attribute
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


# NB: keep in mind, this is not the recommend way to add fields to the user model
user_model = get_user_model() #retrieve the user model
user_model.add_to_class(  #patch the user model
    'following',

    # tell Django to use your custom intermediate model for the relationship by adding through=Contact
    models.ManyToManyField(
        'self',
        related_name='followers',
        through=Contact,
        symmetrical=False
    )
)