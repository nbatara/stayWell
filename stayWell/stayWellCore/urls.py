from django.urls import path
from . import views

app_name = 'stayWellCore'
urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('survey/', views.SurveyView.as_view(), name='Survey'),
    path('complete/', views.CompleteView.as_view(), name='Complete')
]