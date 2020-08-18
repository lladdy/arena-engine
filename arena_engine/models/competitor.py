from django.core.validators import RegexValidator
from django.db import models

from django.conf import settings as django_settings

validate_competitor_name = RegexValidator(r'^[0-9a-zA-Z\._\-]*$',
                                          'Only alphanumeric (A-Z, a-z, 0-9), period (.), underscore (_) '
                                          'and hyphen (-) characters are allowed.')


class Competitor(models.Model):
    user = models.ForeignKey(django_settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='competitors')
    """The user that owns this competitor"""
    name = models.CharField(max_length=50, unique=True, validators=[validate_competitor_name, ])
    """The competitor name"""
    created = models.DateTimeField(auto_now_add=True)
    """When this competitor was first created"""
    active = models.BooleanField(default=False)
    """Whether this competitor is currently active in the season."""

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_not_blank",
                check=(
                    models.Q(
                        name__gt=''
                    )
                ),
            )
        ]
