from django.shortcuts import render
from django.views import generic
from .models import Employee, SurveyEntry, SurveyEntryForm
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django import forms
from django.contrib.auth.models import Permission, User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(generic.ListView):

    # todo: if user request is authenticated send to survey, else send to login
    template_name = 'stayWellCore/index.html'
    context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """ Return the last five published questions. """
#         return None

# def SurveyView(request):
#     newSurvey=SurveyEntry
#     template = loader.get_template('stayWellCore/survey.html')
#     context = {'newSurvey': newSurvey,}
#     return HttpResponse(template.render(context, request))

class SurveyView(LoginRequiredMixin,generic.CreateView):
    login_url = '/signup/'
    model = SurveyEntry
    form_class = SurveyEntryForm
    template_name = 'stayWellCore/survey.html'
    success_url = 'complete/'
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


class CompleteView(generic.ListView):
    template_name = 'stayWellCore/complete.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return None

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    fNumber = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'fNumber', 'email', 'password1', 'password2', )


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.employee.fNumber = form.cleaned_data.get('fNumber')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/survey/')
    else:
        form = SignUpForm()
    return render(request, 'stayWellCore/signup.html', {'form': form})

    # def login(request):
    #     template = loader.get_template('polls/index.html')
    #     return HttpResponse(template.render(request))

    # else:
    #     form = UserCreationForm()
    # return render(request, 'stayWellCore/signup.html', {'form': form})