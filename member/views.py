from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from member.forms import UserForm, UserProfileInfoForm, UserLoginForm

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the site index.")
class index(TemplateView):
    def get(self, request):
        return render(request, 'member/index.html')

class register(View):
    registered = False
    def get(self, request):
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request,'member/registration.html',
                        {'user_form': user_form,
                        'profile_form': profile_form,
                        'registered': self.registered})
    
    def post(self, request):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            self.registered = True
            return render(request,'member/registration.html',
                        {'user_form': user_form,
                        'profile_form': profile_form,
                        'registered': self.registered})
        else:
            print(user_form.errors,profile_form.errors)
            return render(request,'member/registration.html',
                        {'user_form': user_form,
                        'profile_form': profile_form,
                        'registered': self.registered})

class user_logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('member:index'))

class user_login(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if form.cleaned_data['next_url'] == '':
                    return HttpResponseRedirect(reverse('member:index'))
                else:
                    return HttpResponseRedirect(form.cleaned_data['next_url'])
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    def get(self, request):
        next_url = request.GET.get('next', '')
        form = UserLoginForm({'next_url': next_url})
        return render(request, 'member/login.html', {'form': form})
