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
from apps.worklogs import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    # path('accounts/',  include('apps.accounts.urls')),
    # path('wikigcodes/', include('apps.wikigcode.urls')),
    path('worklogs/',  include('apps.worklogs.urls')),
    path('', views.index),
    

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# или для большей читаемости
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
