from django.urls import path

from userena import views
from .forms import SignupFormExtra

urlpatterns = [
    # Signup form with custom field
    path('signup/', views.signup,
         {'signup_form': SignupFormExtra, 'template_name': 'accounts/signup_form.html'},
         name='userena_signup'),
]
