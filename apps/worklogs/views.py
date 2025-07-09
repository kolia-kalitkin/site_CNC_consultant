from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from apps.worklogs.models import RecordWorkDay
from apps.worklogs.forms import RecordWorkDayForm


# Получение данных из БД
def index(request):
    form = RecordWorkDayForm()
    records = RecordWorkDay.objects.all()
    context = {'form': form, 'records': records}
    return render(request, 'worklogs/worklogs.html', context)


# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        form = RecordWorkDayForm(request.POST)
        if form.is_valid():
            record = RecordWorkDay()
            record.work_date = form.cleaned_data['work_date']
            record.work_time_start = form.cleaned_data['work_time_start']
            record.work_time_end = form.cleaned_data['work_time_end']
            record.work_plan = form.cleaned_data['work_plan']
            record.save()
    return HttpResponseRedirect('/')