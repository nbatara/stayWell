import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Permission, User
from django.forms import ModelForm
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fNumber = models.CharField(max_length=30)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
    instance.employee.save()

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    class Meta:
        abstract = True

    def __str__(self):
        return self.question_text

class QuestionCharField(Question):
    pass

class QuestionCharTest(Question):
    pass

class QuestionDropDownField(Question):
    choices = models.TextField(max_length=100)
# Create Tuple
    def createChoicesTuple(self):
        return tuple(str(x) for x in str.splitlines(self.choices))

# Update choices
    def addChoice(self, choiceToAdd):
        self.choices = self.choices + '\n' + choiceToAdd

    def __init__(self):
        choice_text = models.CharField(
            max_length=100,
            choices=self.createChoicesTuple(),
            default=None
            )


class QuestionDecField(Question):
    question_text = models.DecimalField(max_digits=5, decimal_places=2)

class QuestionBoolField(Question):
    question_text = models.BooleanField()

# class ChoiceDropDownField(models.Model):
#     question = models.ForeignKey(QuestionDropDownField, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.choice_text

class WorkLocationChoice(models.Model):
    choice_text = models.CharField(max_length=100)
    def __str__(self):
        return self.choice_text

class SymptomsChoice(models.Model):
    choice_text = models.CharField(max_length=100)
    def __str__(self):
        return self.choice_text

class SurveyEntry(models.Model):

    # INFORMATION AUTOMATICALLY OBTAINED:
    timeStamp = models.DateTimeField(auto_now_add=True)

    # User identification information that can be obtained from request.user
    fNum        = Employee.fNumber
    # userName    = User.username
    firstName   = User.first_name
    lastName    = User.last_name
    
    # INFORMATION INPUT BY THE USER:

    workLocation = models.ManyToManyField(WorkLocationChoice)
    
    Temperature = models.DecimalField(max_digits=5, decimal_places=2)

    Symptoms = models.ManyToManyField(SymptomsChoice)

    otherSymptoms=models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.timeStamp)

class SurveyEntryForm(forms.ModelForm):
    # otherSymptoms = forms.CharField(required=False) 
    # workLocation = forms.ModelChoiceField(queryset=WorkLocationChoice.objects.all(),widget=forms.Select,required=True, empty_label=None)
    # Symptoms = forms.ModelMultipleChoiceField(queryset=SymptomsChoice.objects.all(),widget=forms.CheckboxSelectMultiple,required=True)
    class Meta:
        model = SurveyEntry
        fields = ['workLocation', 'Temperature', 'Symptoms', 'otherSymptoms']
        labels = {'workLocation': 'Work Location', 'otherSymptoms': 'Other Symptoms',}
        # widgets = {
        #     'workLocation': forms.Select,
        # }
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['otherSymptoms'].required = False


