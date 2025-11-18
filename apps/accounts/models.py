from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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
    
    
    # изменение размера изображений
    # Данный код открывает изображение и проверяет, имеет ли оно размер больше 100x100 пикселей. Если это так, изменит размер изображения и сохранит его по тому же пути, по которому он был изначально сохранен (переопределив исходное большое изображение).
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)