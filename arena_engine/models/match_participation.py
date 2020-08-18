from django.db import models

from arena_engine.models import Match, Competitor


class MatchParticipation(models.Model):
    """A competitor's participation in a specific match."""
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='match_participants')
    """The match the competitor is participating in"""
    competitor = models.ForeignKey(Competitor, on_delete=models.PROTECT, related_name='match_participations')
    """The competitor this match participant relates to"""
    participant_number = models.PositiveSmallIntegerField()
    """The number of this match participant"""
    starting_elo = models.SmallIntegerField(null=True)
    """The bot's ELO at the time the match started
    Note that this isn't necessarily the same as resultant_elo - elo_change."""
    resultant_elo = models.SmallIntegerField(null=True)
    """The bot's ELO as a result of this match.
    Note that this isn't necessarily the same as starting_elo + elo_change."""
    elo_change = models.SmallIntegerField(null=True)
    """The amount the competitor's ELO changed as a result of this match."""

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_participant_number",
                fields=['match', 'participant_number'],
            )
        ]

        unique_together = [['match', 'participant_number'], ]
        """Make sure the participant number is unique per match"""
