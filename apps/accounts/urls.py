from django.urls import path
from .views import SignUpView, CustomLoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'), # redirect_authenticated_user=True означает, что пользователи, пытающиеся получить доступ к странице входа после аутентификации, будут перенаправлены обратно
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'), 
]