import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        time = timezone.now() + datetime.timedelta(days=1)
        return Question.objects.create(question_text="question", pub_date=time)
    
    def test_questions_text(self):
        question = Question.objects.get(id=1)
        expected_question_text = f'{question.question_text}'
        self.assertEquals(expected_question_text, "question")