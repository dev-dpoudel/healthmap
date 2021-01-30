# Provides additional Mixins for User / Owner Objects
from django.db import models
from django.contrib.auth import get_user_model


# Get Default User
def get_defaultUser():
    return get_user_model().objects.get(username='alfaaz')[0]


# Provides a shared user property to fetch created_by id
class HiddenOwnerMixin(models.Model):

    @property
    def user(self):
        """ Returns the user of the thread comment """
        return self.created_by

    class Meta:
        abstract = True
