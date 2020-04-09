from django.shortcuts import render
from django.views import generic
from .models import Question, SurveyEntry, SurveyEntryForm
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader


# Create your views here.

class HomeView(generic.ListView):

    # todo: if user request is authenticated send to survey, else send to login
    template_name = 'stayWellCore/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        return None

# def SurveyView(request):
#     newSurvey=SurveyEntry
#     template = loader.get_template('stayWellCore/survey.html')
#     context = {'newSurvey': newSurvey,}
#     return HttpResponse(template.render(context, request))

class SurveyView(generic.CreateView):
    model = SurveyEntry
    form_class = SurveyEntryForm
    template_name = 'stayWellCore/survey.html'
    success_url = 'stayWellCore/complete.html'
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

class CompleteView(generic.ListView):
    template_name = 'stayWellCore/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]