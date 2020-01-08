# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for future questions
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=2)
        future_question2 = Question(pub_date=time)
        self.assertIs(future_question2.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        future_question3 = Question(pub_date=time)
        self.assertIs(future_question3.was_published_recently(), True)
