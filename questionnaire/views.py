from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Questionnaire, Question, Choice, Questionnaire_Results
from .forms import Results_form

# Create your views here.
class Index(View):
    def get(self, request):
        questionnaires = None
        if request.user.is_authenticated:
            questionnaires = Questionnaire.objects.filter(user=request.user)
        return render(request, 'questionnaire/index.html',
                    {'questionnaire_list': questionnaires})

class Create_Questionnaire(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'questionnaire/create.html')

    def post(self, request):
        questionnaire = Questionnaire()
        questionnaire.questionnaire_title = request.POST['questionnaire_title']
        questionnaire.questionnaire_description = request.POST['questionnaire_description']
        questionnaire.user = request.user
        questionnaire.save()
        for key in request.POST.keys():
            key_split = key.split('_')
            if 'question' in key_split:
                if 'choice' in key_split:
                    choice = Choice()
                    choice.choice_text = request.POST[key]
                    choice.question = question
                    choice.save()
                elif key.endswith('allowed_mutiple_answers'):
                    question.is_mutiple_answers = True
                    question.save()
                else:
                    question = Question()
                    question.question_text = request.POST[key]
                    question.questionnaire = questionnaire
                    question.is_mutiple_answers = False
                    question.save()
        return render(request, 'questionnaire/create.html')

class Delete_Questionnaire(LoginRequiredMixin, View):
    succeed = False
    def get(self, request, questionnaire_id):
        qeustionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, user=request.user)
        return render(request, 'questionnaire/delete.html',
                      {'questionnaire': qeustionnaire, 'delete_succeed': self.succeed})

    def post(self, request, questionnaire_id):
        qeustionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, user=request.user)
        qeustionnaire.delete()
        self.succeed = True
        return render(request, 'questionnaire/delete.html',
                      {'delete_succeed': self.succeed})

class Edit_Questionnaire(LoginRequiredMixin, View):
    is_updated = False
    def get(self, request, questionnaire_id):
        qeustionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, user=request.user)
        return render(request, 'questionnaire/edit.html',
                      {'questionnaire': qeustionnaire})

    def post(self, request, questionnaire_id):
        questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id, user=request.user)
        questionnaire.questionnaire_title = request.POST['questionnaire_title']
        questionnaire.questionnaire_description = request.POST['questionnaire_description']
        questionnaire.save()
        keys = request.POST.keys()

        for key in keys:
            key_set = key.split('_')
            if 'question' in key_set:
                question_id = int(key_set[-2])
                try:
                    question = Question.objects.get(pk=question_id)
                    if key_set[0] == 'delete':
                        question.delete()
                    else:
                        question.question_text = request.POST[key]
                        if str(question_id)+'_allowed_mutiple_answers' in keys:
                            question.is_mutiple_answers = True
                        else:
                            question.is_mutiple_answers = False
                        question.save()
                except question.DoesNotExist:
                    print('Question {} does not exist.'.format(question_id))
            elif 'choice' in key_set:
                choice_id = int(key_set[-2])
                try:
                    choice = Choice.objects.get(pk=choice_id)
                    if key_set[0] == 'delete':
                        choice.delete()
                    else:
                        choice.choice_text = request.POST[key]
                        choice.save()
                except choice.DoesNotExist:
                    print('choice {} does not exist.'.format(choice_id))
        self.is_updated = True
        return render(request, 'questionnaire/edit.html',
                      {'questionnaire': questionnaire, 'is_updated': self.is_updated})

class Fill_out_the_questionnaire(View):
    def get(self, request, questionnaire_id):
        qeustionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
        questionnaire_results = Questionnaire_Results()
        return render(request, 'questionnaire/fillOut.html',
                      {'questionnaire': qeustionnaire,
                       'questionnaire_results': questionnaire_results})
    
    def post(self, request, questionnaire_id):
        questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
        questionnaire_results = Questionnaire_Results()
        questionnaire_results.questionnaire = questionnaire
        questionnaire_results.birthday = request.POST['birthday']
        questionnaire_results.gender = request.POST['gender']
        questionnaire_results.education = request.POST['education']
        questionnaire_results.annual_income = request.POST['annual_income']
        questionnaire_results.save()
        for key in request.POST.keys():
            if key.startswith('choice'):
                choice = Choice.objects.get(pk=key.split('-')[1])
                questionnaire_results.choice.add(choice)
        questionnaire_results.save()
        return render(request, 'questionnaire/fillOut.html',
                      {'questionnaire': questionnaire,
                       'questionnaire_results': questionnaire_results})
