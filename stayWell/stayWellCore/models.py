import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    NO_SELECTION = None
    TYPE_1 = 'CharField'
    TYPE_2 = 'DecimalField'
    TYPE_CHOICES = [
        (NO_SELECTION, 'Select Type'),
        (TYPE_1, 'CharField'),
        (TYPE_2, 'DecimalField'),
    ]
    question_text = models.CharField(max_length=200)
    choice_type = models.CharField(
        max_length=200,
        choices=TYPE_CHOICES,
        default=TYPE_1
    )
    possible_choices = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text 

class JournalEntry(models.Model):

    # INFORMATION AUTOMATICALLY OBTAINED:
    timeStamp = models.DateTimeField(auto_now_add=True)

    # User identification information that can be obtained from request.user
    fNum        = '100'
    firstName   = 'firstName'
    lastName    = 'lastName'
    
    # INFORMATION INPUT BY THE USER:

    # station is a selectable choice from all registered stations
    NO_SELECTION = None
    STATION_1 = 'Station 1'
    STATION_2 = 'Station 2'
    STATION_3 = 'Station 3'
    STATION_N = 'Station N'
    STATION_CHOICES = [
        (NO_SELECTION, 'Select Station'),
        (STATION_1, 'Station 1'),
        (STATION_2, 'Station 2'),
        (STATION_3, 'Station 3'),
        (STATION_N, 'Station N')
    ]
    station = models.CharField(
        max_length=100,
        choices=STATION_CHOICES,
        default=NO_SELECTION
    ) # select from dropdown of registeredStations
    
    Temperature = models.DecimalField(max_digits=5, decimal_places=2)

    otherSymptoms = models.CharField(max_length=100)
    # List that contains all selectable symptons
    trackedAdditionalSymptoms = [
        'Symptom 1',
        'Symptom 2',
        'Symptom n',
    ]


    
    
    
    temperature = None # enter temperature in °F, could be text-box with entry parsing, or selectable wheel, etc.
    additionalSymptoms = dict.fromkeys(trackedAdditionalSymptoms, False) # create dictionary of trackedAdditionalSymptoms, initialized to False.
    otherSymptoms = models.CharField(max_length=200) # entry field for users to input other additional symptoms

