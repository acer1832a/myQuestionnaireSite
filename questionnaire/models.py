from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questionnaire(models.Model):
    questionnaire_title = models.CharField(max_length=100)
    questionnaire_description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.questionnaire_title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    is_mutiple_answers = models.BooleanField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text