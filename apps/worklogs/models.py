from django.db import models


class Employee(models.Model):
    employee = models.TextField()




class RecordWorkDay(models.Model):
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_date = models.DateField()
    work_time_start = models.DateField()
    work_time_end = models.DateField()
    text = models.TextField()
    

    def __str__(self) -> str:
        return f'запись от {str(self.work_date)}'
    

    class Meta:
        verbose_name = 'Запись учета рабочего дня'
        verbose_name_plural = 'Записи учета рабочего дня'