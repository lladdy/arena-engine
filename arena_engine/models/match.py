from django.db import models

from arena_engine.models.round import Round


class Match(models.Model):
    """A match played between a number of teams."""
    created = models.DateTimeField(auto_now_add=True)
    """The datetime this match record was created"""
    started = models.DateTimeField(blank=True, null=True, editable=False)
    """The datetime this match started playing"""
    round = models.ForeignKey(Round, on_delete=models.CASCADE, blank=True, null=True)
    """The round, if any, that this match was played as a part of"""
