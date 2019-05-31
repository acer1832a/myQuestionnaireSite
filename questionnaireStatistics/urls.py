from django.urls import include, path
from rest_framework import routers
from .views import ChoiceViewSet, QuestionViewSet, QuestionnaireViewSet, QuestionnaireStatisticsView, QuestionnaireResultsViewSet

app_name = 'statistics'

router = routers.DefaultRouter()
router.register('choice', ChoiceViewSet)
router.register('question', QuestionViewSet)
router.register('questionnaire', QuestionnaireViewSet)
router.register('questionnaireResults', QuestionnaireResultsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('questionnaire/<int:questionnaire_id>/', QuestionnaireStatisticsView.as_view())
]