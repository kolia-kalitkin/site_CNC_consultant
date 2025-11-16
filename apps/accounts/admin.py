# импортируем модель профиля, а затем вызывает admin.site.register для ее регистрации
from apps.accounts.models import Profile
from django.contrib import admin

admin.site.register(Profile) 
