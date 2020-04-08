from django.shortcuts import render
from django.views import generic
from .models import Question
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


# Create your views here.

class HomeView(generic.ListView):
    template_name = 'stayWellCore/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        return None

class SurveyView(generic.ListView):
    template_name = 'stayWellCore/survey.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class CompleteView(generic.ListView):
    template_name = 'stayWellCore/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]