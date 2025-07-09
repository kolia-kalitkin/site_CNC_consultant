from django.db import models
from django.contrib.auth.models import User


class RecordWorkDay(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_date = models.DateField()
    work_time_start = models.DateField()
    work_time_end = models.DateField()
    work_plan = models.TextField()
        

    def __str__(self) -> str:
        return f'запись от {str(self.work_date)}'
    

    class Meta:
        verbose_name = 'Запись учета рабочего дня'
        verbose_name_plural = 'Записи учета рабочего дня'