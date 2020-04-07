from django.urls import path
from . import views

app_name = 'stayWellCore'
urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
]