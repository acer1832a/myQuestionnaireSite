from django.urls import path
from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('CreateNewQuestionnaire/', views.Create_Questionnaire.as_view() , name='create'),
    path('<int:questionnaire_id>/delete/', views.Delete_Questionnaire.as_view(), name='delete'),
    path('<int:questionnaire_id>/edit/', views.Edit_Questionnaire.as_view(), name='edit'),
    path('<int:questionnaire_id>/', views.Fill_out_the_questionnaire.as_view(), name='fillOut'),
]