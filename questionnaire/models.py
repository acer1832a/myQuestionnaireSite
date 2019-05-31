from django.db import models
from django.contrib.auth.models import User
from accounts.models import MyProfile

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

    @property
    def counts(self):
        return self.questionnaire_results_set.count()
    
    def __str__(self):
        return self.choice_text

class Questionnaire_Results(models.Model):
    GENDER_CHOICES = MyProfile.GENDER_CHOICES
    ANNUAL_INCOME_CHOICES = MyProfile.ANNUAL_INCOME_CHOICES
    EDUCATION_CHOICES = MyProfile.EDUCATION_CHOICES

    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthday = models.DateField()
    education = models.CharField(max_length=1, choices=EDUCATION_CHOICES)
    annual_income = models.IntegerField(choices=ANNUAL_INCOME_CHOICES)
    choice = models.ManyToManyField(Choice)
    fill_time = models.DateTimeField(auto_now_add=True)
