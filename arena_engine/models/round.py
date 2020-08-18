from django.core.validators import RegexValidator
from django.db import models

from django.conf import settings as django_settings


class Round(models.Model):
    """A round of matches. A generic grouping of matches.
    Usually a round-robin round, but could be used in other ways."""
    pass
