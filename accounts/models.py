from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    MALE = 'Male'
    FEMALE = 'Female'
    THIRD_SEX = 'Others'
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (THIRD_SEX, _('Other')),
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
        (JUNIOR_HIGH_SCHOOL, _('junior high school')),
        (HIGH_SCHOOL, _('high school')),
        (BACHELOR, _('bachelor')),
        (MASTER, _('master')),
        (DOCTOR, _('doctor')),
    )

    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile',
                                on_delete=models.CASCADE)
    gender = models.CharField(_('gender'), max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    education = models.CharField(_('education'), max_length=1, choices=EDUCATION_CHOICES, blank=True, null=True)
    annual_income = models.IntegerField(_('annual income'), choices=ANNUAL_INCOME_CHOICES, blank=True, null=True)
