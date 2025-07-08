from django.db import models


from django.db import models

class Info(models.Model):
    text = models.TextField()
    

    # def __str__(self) -> str:
    #     return 'Модель отображения информации'