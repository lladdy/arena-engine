from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

from arena_engine.models.competitor import Competitor


class CompetitorsTestCase(TestCase):

    def test_name_validation_none(self):
        user = User.objects.create()
        with self.assertRaisesRegexp(IntegrityError,
                                     'new row for relation "arena_engine_competitor" '
                                     'violates check constraint "arena_engine_competitor_not_blank".*'):
            Competitor.objects.create(user=user)

    def test_name_validation_blank(self):
        user = User.objects.create()
        with self.assertRaisesRegexp(IntegrityError,
                                     'new row for relation "arena_engine_competitor" '
                                     'violates check constraint "arena_engine_competitor_not_blank".*'):
            Competitor.objects.create(user=user, name='')

    def test_name_validation_invalid_characters(self):
        user = User.objects.create()
        user.save()
        Competitor.objects.create(user=user, name='!@#$%^&*()')

    def test_name_validation_valid_characters(self):
        user = User.objects.create()
        Competitor.objects.create(user=user, name='qwertyuiopasdfghjklzxcvbnm1234567890-_.')


