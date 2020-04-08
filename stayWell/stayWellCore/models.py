import datetime
from django.db import models
from django.utils import timezone

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
    pass


class QuestionDecField(Question):
    question_text = models.DecimalField(max_digits=5, decimal_places=2)

class QuestionBoolField(Question):
    question_text = models.BooleanField()

class ChoiceDropDownField(models.Model):
    question = models.ForeignKey(QuestionDropDownField, on_delete=models.CASCADE)
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
    def __str__(self):
        return self.choice_text

class SurveyEntry(models.Model):

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

