from django.db import models
from apps.services.utils import unique_slugify

class Info(models.Model):
    title = models.CharField(max_length=100, default='Статья')
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата публикации')
    
    class Meta:
        """
        Сортировка, название таблицы в базе данных
        """
        ordering = ('publication_date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title, self.slug)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title[:20]