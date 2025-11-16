from django.db import models
from django.contrib.auth.models import User

# модель профиля
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     # при удалении пользователя удаляется и его профиль
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')   # изображение по умолчанию и каталог, в который загружаются изображения. # поле ImageField как и поле FileField не хранит загруженные файлы в БД, а только ссылки на них.
    user_information = models.TextField()

    class Meta:
        """
        Сортировка,
        название таблицы в базе данных,
        """
        ordering = ('user',)
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


    def __str__(self):
        return self.user.username
    
    
