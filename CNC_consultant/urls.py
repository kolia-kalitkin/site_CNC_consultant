"""
URL configuration for CNC_consultant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from apps.main.views import index
# from apps.worklogs.views import get_from_db

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')), # сначала в наше приложение accounts, и только потом в auth:
    path('accounts/', include('django.contrib.auth.urls')), # подключаем маршруты встроенное приложение авторизации auth 
    path('wikigcodes/', include('apps.wikigcode.urls')),
    path('worklogs/',  include('apps.worklogs.urls')),    
    path('', include('apps.main.urls')),  # главная страница

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# или для большей читаемости
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
