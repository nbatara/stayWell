from django.contrib import admin

from .models import QuestionCharField, QuestionDropDownField, SurveyEntry
# Register your models here.
admin.site.register(QuestionCharField)
admin.site.register(QuestionDropDownField)
admin.site.register(SurveyEntry)

