import django
from django.db import models
from django.utils import timezone
import django.utils
import django.utils.timezone
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    question_author = models.CharField(max_length = 100, default="Анонимно")
    question_date = models.DateTimeField("Время создания вопроса", default=django.utils.timezone.now)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 100)
    votes = models.IntegerField(default=0)
