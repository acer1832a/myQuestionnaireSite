from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.db.models import Count
from questionnaire.models import Questionnaire, Question, Choice, Questionnaire_Results
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers

class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer

class QuestionnaireViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = serializers.QuestionnaireSerializer

    @action(methods=['get'], detail=True, url_path='get-gender-count', url_name='get_gender_count')
    def get_gender_count(self, request, pk=None):
        gender_dict = dict(Questionnaire_Results.GENDER_CHOICES)
        queryset = Questionnaire_Results.objects.all().filter(questionnaire_id=pk).values('gender').annotate(total=Count('gender'))
        for data in queryset:
            data['gender'] = gender_dict[data['gender']]
        serializer = serializers.GenderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True, url_path='get-education-count', url_name='get_education_count')
    def get_education_count(self, request, pk=None):
        education_dict = dict(Questionnaire_Results.EDUCATION_CHOICES)
        queryset = Questionnaire_Results.objects.all().filter(questionnaire_id=pk).values('education').annotate(total=Count('education'))
        for data in queryset:
            data['education'] = education_dict[data['education']]
        serializer = serializers.EducationSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True, url_path='get-annual-income-count', url_name='get_annual_income_count')
    def get_annual_income_count(self, request, pk=None):
        annual_income_dict = dict(Questionnaire_Results.ANNUAL_INCOME_CHOICES)
        queryset = Questionnaire_Results.objects.all().filter(questionnaire_id=pk).values('annual_income').annotate(total=Count('annual_income'))
        for data in queryset:
            data['annual_income'] = annual_income_dict[data['annual_income']]
        serializer = serializers.AnnualIncomeSerializer(queryset, many=True)
        return Response(serializer.data)

class QuestionnaireResultsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Questionnaire_Results.objects.all()
    serializer_class = serializers.QuestionnaireResultsSerializer

class QuestionnaireStatisticsView(View):
    def get(self, request, questionnaire_id):
        questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
        return render(request, 'questionnaireStatistics/questionnaire.html',
                     {'questionnaire': questionnaire})
