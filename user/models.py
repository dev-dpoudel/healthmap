from django.db import models  # noqa : F401 Unused Import
from django.contrib.auth.models import AbstractUser

# User Class for Custom AuthenticationMiddleware.


class User (AbstractUser):
    pass
