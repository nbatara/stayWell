from django.urls import path, include
from . import views

app_name = 'stayWellCore'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='signup'),
    # path('accounts/', include('django.contrib.auth.urls')),   
    path('', views.HomeView.as_view(), name='Home'),
    path('survey/', views.SurveyView.as_view(), name='Survey'),
    path('survey/complete/', views.CompleteView.as_view(), name='Complete')
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]