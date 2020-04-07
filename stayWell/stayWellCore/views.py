from django.shortcuts import render

# Create your views here.
class HomeView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date').exclude(choice=None)[:5]