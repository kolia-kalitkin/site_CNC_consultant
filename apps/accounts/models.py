from django.db import models
from django.contrib.auth.models import User
from apps.services.utils import unique_slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    job_title = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    machine = models.CharField(max_length=50, blank=True, verbose_name='Обслуживаемый станок',)
    info_about_yourself = models.TextField(max_length=500, blank=True, verbose_name='Информация о себе')

    
    class Meta:
        """
        Сортировка, название таблицы в базе данных
        """
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.user.username, self.slug)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.user.username
    