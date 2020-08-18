from unittest import TestCase

from django.contrib.auth.models import User
from django.db import IntegrityError

from arena_engine.models import Competitor, Match, MatchParticipation


class MatchParticipantTestCase(TestCase):

    def test_unique_participant_number_per_match(self):
        u1 = User.objects.create()
        c1 = Competitor.objects.create(name='Competitor1', user=u1)
        c2 = Competitor.objects.create(name='Competitor2', user=u1)
        match = Match.objects.create()
        with self.assertRaisesRegexp(IntegrityError,
                                     'duplicate key value violates unique constraint '
                                     '"arena_engine_matchparticipant_unique_participant_number".*'):
            MatchParticipation.objects.create(competitor=c1, match=match, participant_number=1)
            MatchParticipation.objects.create(competitor=c2, match=match, participant_number=1)
