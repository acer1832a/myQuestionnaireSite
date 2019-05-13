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

class Questionnaire_Results(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    THIRD_SEX = 'Others'
    GENDER_CHOICES = (
        (MALE, '男性'),
        (FEMALE, '女性'),
        (THIRD_SEX, '其它'),
    )

    ANNUAL_INCOME_BELOW_20W = 20
    ANNUAL_INCOME_20W_40W = 40
    ANNUAL_INCOME_40W_60W = 60
    ANNUAL_INCOME_60W_100W = 100
    ANNUAL_INCOME_OVER_100W = 101
    ANNUAL_INCOME_CHOICES = (
        (ANNUAL_INCOME_BELOW_20W, '20萬以下'),
        (ANNUAL_INCOME_20W_40W, '21萬至40萬'),
        (ANNUAL_INCOME_40W_60W, '41萬至60萬'),
        (ANNUAL_INCOME_60W_100W, '61萬至100萬'),
        (ANNUAL_INCOME_OVER_100W, '100萬以上'),
    )

    JUNIOR_HIGH_SCHOOL = 'J'
    HIGH_SCHOOL = 'H'
    BACHELOR = 'B'
    MASTER = 'M'
    DOCTOR = 'D'
    EDUCATION_CHOICES = (
        (JUNIOR_HIGH_SCHOOL, '國中'),
        (HIGH_SCHOOL, '高中'),
        (BACHELOR, '大學'),
        (MASTER, '碩士'),
        (DOCTOR, '博士'),
    )
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthday = models.DateField()
    education = models.CharField(max_length=1, choices=EDUCATION_CHOICES)
    annual_income = models.IntegerField(choices=ANNUAL_INCOME_CHOICES)
    choice = models.ManyToManyField(Choice)
    fill_time = models.DateTimeField(auto_now_add=True)
