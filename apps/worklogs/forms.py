from django import forms
from django.forms import ModelForm, DateField, TimeField, CharField
from apps.worklogs.models import RecordWorkDay

class RecordWorkDayForm(ModelForm):
    work_date = DateField(label='Укажите дату')
    work_time_start = TimeField(label='Время начала')
    work_time_end = TimeField(label='Время окончания')
    work_plan = CharField(label='Укажите выполненную работу', widget=forms.Textarea)
    

    class Meta:
        model = RecordWorkDay
        fields = ['work_date', 'work_time_start', 'work_time_end', 'work_plan',]




   