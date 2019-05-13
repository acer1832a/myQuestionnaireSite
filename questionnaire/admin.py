from django.contrib import admin
from .models import Questionnaire, Question, Choice, Questionnaire_Results

# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Questionnaire_Results)