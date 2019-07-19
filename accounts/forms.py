from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupForm
from .models import MyProfile

class SignupFormExtra(SignupForm):
    blank_choice = (('', _('Please choose an option')),)
    gender = forms.ChoiceField(label=_(u'gender'), choices=blank_choice+MyProfile.GENDER_CHOICES, required=False)
    birthday = forms.DateField(label=_(u'birthday'), required=False)
    education = forms.ChoiceField(label=_(u'education'), choices=blank_choice+MyProfile.EDUCATION_CHOICES, required=False)
    annual_income = forms.ChoiceField(label=_(u'annual income'), choices=((0, _('Please choose an option')),)+MyProfile.ANNUAL_INCOME_CHOICES, required=False)

    def __init__(self, *args, **kw):
        """
        A bit of hackery to get the first name and last name at the top of the
        form instead at the end.
        """
        super(SignupFormExtra, self).__init__(*args, **kw)

    def save(self):
        """
        Override the save method to save the first and last name to the user
        field.
        """
        # First save the parent form and get the user.
        new_user = super(SignupFormExtra, self).save()

        # Get the profile, the `save` method above creates a profile for each
        # user because it calls the manager method `create_user`.
        # See: https://github.com/django-userena-ce/django-userena-ce/blob/master/userena/managers.py#L65
        profile = new_user.my_profile
        profile.gender = self.cleaned_data['gender']
        profile.education = self.cleaned_data['education']
        profile.birthday = self.cleaned_data['birthday']
        profile.annual_income = self.cleaned_data['annual_income']
        profile.save()

        # Userena expects to get the new user from this form, so return the new
        # user.
        return new_user
