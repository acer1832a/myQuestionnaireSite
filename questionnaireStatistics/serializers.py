from rest_framework import serializers
from questionnaire.models import Questionnaire, Question, Choice, Questionnaire_Results
from django.db.models import Field

class ChoiceSerializer(serializers.ModelSerializer):
    counts = serializers.ReadOnlyField()
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(read_only=True, many=True)
    class Meta:
        model = Question
        depth = 1
        fields = '__all__'

class QuestionnaireResultsSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')
    education = serializers.CharField(source='get_education_display')
    annual_income = serializers.CharField(source='get_annual_income_display')
    class Meta:
        model = Questionnaire_Results
        fields = '__all__'

class QuestionnaireSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(read_only=True, many=True)
    questionnaire_results_set = QuestionnaireResultsSerializer(read_only=True, many=True)
    class Meta:
        model = Questionnaire
        depth = 1
        fields = '__all__'

class GenderSerializer(serializers.Serializer):
    gender = serializers.CharField()
    total = serializers.IntegerField()

class EducationSerializer(serializers.Serializer):
    education = serializers.CharField()
    total = serializers.IntegerField()

class AnnualIncomeSerializer(serializers.Serializer):
    annual_income = serializers.CharField()
    total = serializers.IntegerField()
